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

class MyUserCreationForm(UserCreationForm):
    # is_human = forms.BooleanField(label = "Are you human?:")
    # firstname = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=255, label = "Фамилия")
    # fieldsets = ('username', 'lastname', 'password1', 'password2')
    # fieldsets = ('lastname', 'password1', 'password2')
    # на fieldseets не реагирует

    # class Meta:
    #     model = UserCreationForm
    #     fields = ('username', 'lastname', 'password1', 'password2')
    #
    # fieldsets = ('username', 'lastname', 'password1', 'password2')
    # fieldsets = ((None, {'fields': ('image', 'name',)}),)


class MySignupView(CreateView):
   form_class = MyUserCreationForm # выше добавил фамилию
   success_url = '/login'
   template_name = 'accounts/register.html'

# from django.contrib.auth.views import LoginView

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'accounts/login.html'
