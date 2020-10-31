from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm
from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView
)
from users.models import Profile

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

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

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
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def home(request):
    return render(request, 'blog/index.html')


# def DashboardView(request):
#     donations = Donation.objects.filter(donor=request.user)
#     recieved = Donation.objects.filter(receiver=request.user)
#     context = {
#         'donations': donations,
#         'recieved': recieved
#     }
#     return render(request, 'blog/dashboard.html', context)

def FilteredHospitalView(request, cats):
    category_posts = []
    # users = Profile.objects.filter(Hospital=cats)
    posts = Post.objects.all()
    for post in posts:
       if post.author.profile.Hospital == cats:
           category_posts.append(post)

    return render(request, 'blog/categories.html', {'cats': cats, 'category_posts': category_posts})

def FilteredCityView(request, cats):
    print('random shit')
    category_posts = []
    users = Profile.objects.filter(city=cats)
    posts = Post.objects.all()
    print(posts)
    for post in posts:
        
        if post.author.profile.city == cats:
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