from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm as Registeration,AuthenticationForm as Login
from django.contrib.auth import get_user_model
from django import forms
class UserCreationForm(Registeration):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserCreationForm, self).__init__(*args, **kwargs)
    class Meta:
        model=get_user_model()
        fields=['username','last_name','password1','password2',]
    
    
    # def clean(self):
    #     super().clean()
    #     username = self.cleaned_data['username']
    #     password = self.cleaned_data['password1']
    #     self.user_cache = authenticate(request=self.request,username=username,password=password)
    #     print(self.user_cache)
    #     if self.user_cache is None:
    #         raise forms.ValidationError("Invalid email or password")
    #     elif not self.user_cache.is_active:
    #         raise forms.ValidationError("This account is inactive")
    #     return self.cleaned_data

# def save(self, commit: bool = True):
#     user = super(UserCreationForm, self).save(commit=False)
#     fname= self.changed_data['name']
#     if commit:
#         user.save()
#     return user