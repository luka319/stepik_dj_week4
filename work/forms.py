from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

# class PostcardForm(forms.Form):
#     address = forms.CharField(label='Destination Address')
#     author = forms.CharField(min_length=3)
#     compliment = forms.CharField(max_length=1024)
#     date_of_delivery = forms.DateField(input_formats=['%Y/%m/%d'])
#     email = forms.EmailField()
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.add_input(Submit('submit', 'Submit'))

# from django.contrib.auth.forms import UserCreationForm
# from django.views.generic import CreateView

class MySignupView(CreateView):
   form_class = UserCreationForm
   success_url = '/login'
   template_name = 'signup.html'

# from django.contrib.auth.views import LoginView

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'
