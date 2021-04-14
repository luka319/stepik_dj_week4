from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User

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
# from django import forms
# from django.contrib.auth.models import User
# по мотивам: https://coderoad.ru/5745197/Django-создать-пользовательскую-форму-UserCreationForm

class MyUserCreationForm(UserCreationForm):
    # is_human = forms.BooleanField(label = "Are you human?:")
    # firstname = forms.CharField(max_length=30)
    # lastname = forms.CharField(max_length=255, label = "Фамилия")
    class Meta:
        model = User
        fields = ('username', 'last_name', 'password1', 'password2')

    # Привет! У    базовой    модели    пользователя    есть
    # поле    last_name.Чтобы    это    поле    можно
    # было    заполнить    через    форму, просто
    # добавь    его    в    Meta.fields

# Теперь нужно переопределить метод save, однако, поскольку
# модель пользователя не имеет поля lastname,
# она должна выглядеть следующим образом:

    def save(self, commit=True):
        user = super(MyUserCreationForm, self).save(commit=True)
        last_name = self.cleaned_data["last_name"]
        user.last_name = last_name
        ## user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class MySignupView(CreateView):
   form_class = MyUserCreationForm # выше добавил фамилию
   success_url = 'login/'
   template_name = 'accounts/register.html'

# from django.contrib.auth.views import LoginView

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'accounts/login.html'
