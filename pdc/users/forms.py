from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, DonorDetails

GENDER=[('male','Male'),('female','Female'),('others','Others'),]
BLOODGROUP=[('O+','O+'),('A+','A+'),('B+','B+'),('AB+','AB+'),('O-','O-'),('A-','A-'),('B-','B-'),('AB-','AB-'),]
PREGNANT=[('yes','Yes'),('no','No')]
ANEMIA=[('yes','Yes'),('no','No')]

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", 'email']

class ProfileUpdateForm(forms.ModelForm):
    age =forms.IntegerField()
    gender=forms.CharField(label='What is your gender?',widget=forms.Select(choices=GENDER))
    blood_group=forms.CharField(label='What is your blood Group?',widget=forms.Select(choices=BLOODGROUP))
    district=forms.CharField(max_length=10)
    Hospital=forms.CharField(max_length=10, label='Nearby hospitals?')
    has_corona = forms.CharField(label='Was your COVID test positive?',widget=forms.Select(choices=PREGNANT))
    is_donor = forms.BooleanField(required=False)

    class Meta:
        model = Profile 
        fields = ['image', 'is_donor', 'age', 'gender', 'blood_group',
                   'district', 'Hospital', 'has_corona'
                 ]

class DetailUpdateForm(forms.ModelForm):
    weight=forms.IntegerField()
    pregnant=forms.CharField(max_length=10, widget=forms.Select(choices=ANEMIA))
    anemia=forms.CharField(label='Do you suffer from anemia or low hemoglobin levels?',widget=forms.Select(choices=ANEMIA))
    infectious_diseases=forms.CharField(label='Do you suffer from any infectious diseases like HIV,Hepatitis,TB,Malaria ?',widget=forms.Select(choices=ANEMIA))
    # doctors_prescription=forms.ImageField()
    days=forms.CharField(label='Has it been 14 days since the last day of COVID symptoms?',widget=forms.Select(choices=PREGNANT))
    test=forms.CharField(label='Did you have a follow up covid test?',widget=forms.Select(choices=PREGNANT))
    covid=forms.CharField(label='Was your COVID test positive?',widget=forms.Select(choices=PREGNANT))

    class Meta:
        model = DonorDetails
        fields = ['user', 'weight', "pregnant", "anemia", "infectious_diseases", "doctors_prescription",
            "days", "test", "covid"
        ]