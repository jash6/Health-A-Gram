from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post,Donation
from users.models import Profile
from .forms import PostForm,Form
from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView
)
from django.conf import settings
from django.core.mail import send_mail
from users.models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# def home(request):
#     context = {
#         'posts': Post.objects.all(),
#         'profile': Profile.objects.all()
#     }
#     return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

# class PostDetailView(DetailView):
#     model = Post
@login_required
def PostDetailView(request,pk):
    if request.method== 'POST':
        form=Form(request.POST)
        if form.is_valid():
            form.save()
            donation =Donation()
            post = get_object_or_404(Post, pk=pk)
            donation.receiver= request.user
            donation.donor= post.author
            donation.City= post.author.profile.district
            donation.Hospital = post.author.profile.Hospital
            donation.save()
            send_mail('Health-a-gram has some great news for you',f' {request.user} ({request.user.email}) needs your help!',settings.EMAIL_HOST_USER,[f'{post.author.email}'],fail_silently=False)
            messages.success(request, f'We have notified the Donor, thankyou for the using Health-a-gram')
            return redirect('dash-view')
        else:
            pass
    else:
        form=Form()
        context = {
            "form": form,
            "post": get_object_or_404(Post, pk=pk),
        }
        return render(request,'blog/post_detail.html',{
                "form": form,
                "post": get_object_or_404(Post, pk=pk),
            })


@login_required
def PostCreateView(request):
    if request.method== 'POST':
        form=PostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            post  = form.save() 
            post_bg = post.author.profile.blood_group
            post_dis = post.author.profile.district
            patients = Profile.objects.all().filter(is_donor= False)
            for patient in patients:
                patient_bg = patient.blood_group
                if request.user != patient.user:
                    if patient.district == post_dis:
                        if post_bg[-1] == '+' and patient_bg[-1]=='+':
                            if post_bg[0] == 'O' or post_bg == patient_bg or patient_bg == 'AB+':
                                send_mail('News from Health-a-gram, a potential donor is nearby!',f' {request.user} has entered your recommendations',settings.EMAIL_HOST_USER,[f'{patient.user.email}'],fail_silently=False)
                                messages.success(request, f'We have notified the patients')
                        elif post_bg[-1] == '-':
                            if post_bg[0] == 'O' or post_bg[0] == patient_bg[0] or patient_bg[:-1] == 'AB':
                                send_mail('News from Health-a-gram, a potential donor is nearby!',f' {request.user} has entered your recommendations',settings.EMAIL_HOST_USER,[f'{patient.user.email}'],fail_silently=False)
                                messages.success(request, f'We have notified the patients')
                return redirect("recommend")
    else:
        form=PostForm()
        context = {
            "form": form,
        }
        return render(request,'blog/post_form.html',context)

# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     form_class = PostForm

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content','weight', "pregnant", "anemia", "infectious_diseases", "doctors_prescription",
            "days", "test", "covid"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/donate/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def home(request):

    profiles = Profile.objects.all()
    # profiles.append(Profile.objects.filter(blood_group="o+").first())
    # profiles.append(Profile.objects.filter(blood_group="ab+").last())
    # profiles.append(Profile.objects.filter(blood_group="ab+").first())
    # profiles.append(Profile.objects.filter(blood_group="o+").last())

    return render(request, 'blog/index.html', {"profiles": profiles})

def faq(request):
    return render(request, 'blog/faq.html')

def news(request):
    return render(request, 'blog/news.html')

def contact(request):
    return render(request, 'blog/contact.html')


def DashboardView(request):
    donations = Donation.objects.filter(donor=request.user)
    recieved = Donation.objects.filter(receiver=request.user)
    context = {
        'donations': donations,
        'recieved': recieved
    }
    return render(request, 'blog/dashboard.html', context)

def FilteredHospitalView(request, cats):
    category_posts = []
    # users = Profile.objects.filter(Hospital=cats)
    posts = Post.objects.all()
    for post in posts:
       if post.author.profile.Hospital == cats:
           category_posts.append(post)

    return render(request, 'blog/categories.html', {'cats': cats, 'category_posts': category_posts})

def FilteredCityView(request, cats):
    category_posts = []
    users = Profile.objects.filter(district=cats)
    posts = Post.objects.all()
    for post in posts:
        
        if post.author.profile.district == cats:
           category_posts.append(post)

    return render(request, 'blog/categories.html', {'cats': cats, 'category_posts': category_posts})

def FilteredBloodView(request, cats):
    category_posts = []
    users = Profile.objects.filter(blood_group=cats)
    posts = Post.objects.all()
    for post in posts:
       if post.author.profile.blood_group == cats:
           category_posts.append(post)

    return render(request, 'blog/categories.html', {'cats': cats, 'category_posts': category_posts})

def recommend(request):
    category_posts = []
    posts = Post.objects.all()
    user_bg = request.user.profile.blood_group
    user_dis = request.user.profile.district

    for post in posts:
        if post.author.profile.district == user_dis:
            post_bg = post.author.profile.blood_group

            if user_bg[-1] == '-' and post_bg[-1]=='-':
                if user_bg[0] == post_bg[0] or post_bg == 'O-' or user_bg[-2] == post_bg[0]:
                    category_posts.append(post)
            elif user_bg[-1] == '+':
                if user_bg[0] == post_bg[0] or post_bg[0] == 'O' or user_bg[-2] == post_bg[0]:
                    category_posts.append(post)

    if len(category_posts) >= 1:
        return render(request, 'blog/categories.html', {'category_posts': category_posts})
    else:
        return render(request, 'blog/categories.html')

    