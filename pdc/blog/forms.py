from django import forms
from .models import Post

# GENDER=[('male','Male'),('female','Female'),('others','Others'),]
# BLOODGROUP=[('o+','O+'),('a+','A+'),('b+','B+'),('ab+','AB+'),('o-','O-'),('a-','A-'),('b-','B-'),('ab-','AB-'),]
ANEMIA=[('yes','Yes'),('no','No')]
WEIGHT = [('light', 'till 30'), ('medium', 'from 30 to 70'), ('heavy', "above 70")]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content','weight', "pregnant", "anemia", "infectious_diseases", "doctors_prescription",
            "days", "test", "covid"
        )
        widgets = {

            'title' : forms.TextInput(attrs={'class':'form-control'}),
            # 'category': forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'weight' : forms.Select(choices=WEIGHT,attrs={'class':'form-control'}),
            'pregnant' : forms.Select(choices=ANEMIA, attrs={'class':'form-control'}),
            'anemia': forms.Select(choices=ANEMIA,attrs={'class':'form-control'}),
            'infectious_diseases': forms.Select(choices=ANEMIA ,attrs={'class':'form-control'}),
            #'doctors_prescription': forms.Select(choices=ANEMIA, attrs={'class':'form-control'}),
            'days': forms.Select(choices=ANEMIA,attrs={'class':'form-control'}),
            'test': forms.Select(choices=ANEMIA, attrs={'class':'form-control'}),
            'covid': forms.Select(choices=ANEMIA, attrs={'class':'form-control'}),
        
        }

# class PostForm(forms.ModelForm):
#     title = forms.CharField(max_length=20)
#     content = forms.Textarea(max_length=100)
#     weight=forms.IntegerField()
#     pregnant=forms.CharField(max_length=10, widget=forms.Select(choices=ANEMIA))
#     anemia=forms.CharField(label='Do you suffer from anemia or low hemoglobin levels?',widget=forms.Select(choices=ANEMIA))
#     infectious_diseases=forms.CharField(label='Do you suffer from any infectious diseases like HIV,Hepatitis,TB,Malaria ?',widget=forms.Select(choices=ANEMIA))
#     doctors_prescription=forms.CharField(max_length=10)
#     days=forms.CharField(label='Has it been 14 days since the last day of COVID symptoms?',widget=forms.Select(choices=ANEMIA))
#     test=forms.CharField(label='Did you have a follow up covid test?',widget=forms.Select(choices=ANEMIA))
#     covid=forms.CharField(label='Was your COVID test positive?',widget=forms.Select(choices=ANEMIA))

#     class Meta:
#         model = Post
#         fields = ['title', 'content','weight', "pregnant", "anemia", "infectious_diseases", "doctors_prescription",
#             "days", "test", "covid"
#         ]
