from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from django import forms

username_validator = UnicodeUsernameValidator()

class RegisterUserForm(UserCreationForm):
    error_messages = {
        "password_mismatch": ("Пароли не схожи"),
    }
    username = forms.CharField(
        required=True,
        label=("Имя пользователя*"),
        max_length=150,
        help_text=(""),
        validators=[username_validator],
        error_messages={"unique": ("Такой пользователь существует")},
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password1 = forms.CharField(
        required=True,
        label=("Пароль*"),
        widget=(forms.PasswordInput(attrs={"class": "form-control"})),
        help_text="",
    )
    password2 = forms.CharField(
        required=True,
        label=("Подтверждение пароля*"),
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        help_text=("Введите пароль повторно"),
    )
    email = forms.EmailField(
        label="Email*",
        required=True,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Введите email"}
        ),
    )
    first_name = forms.CharField(
        label="Имя*",
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Введите имя"}
        ),
    )
    last_name = forms.CharField(
        label="Фамилия*",
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Введите фамилию"}
        ),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
        ]
        labels = {
            "username": "Имя пользователя",
            "email": "Email",
            "password1": "Пароль",
            "password2": "Подтверждение пароля",
        }

class SupportForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter your email"}
        ),
    )
    subject = forms.CharField(
        label="Subject",
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter subject"}
        ),
    )
    message = forms.CharField(
        label="Message",
        required=True,
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Write your problem"}
        ),
    )