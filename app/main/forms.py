from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from django import forms
from month.widgets import MonthSelectorWidget

from main.models import Treaty, Record

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
        label="Электронная почта",
        required=True,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Напишите свою электронную почту"}
        ),
    )
    subject = forms.CharField(
        label="Тема",
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Напишите тему сообщение"}
        ),
    )
    message = forms.CharField(
        label="Сообщение",
        required=True,
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Опишите свою проблему"}
        ),
    )


class TreatyForm(forms.ModelForm):
    class Meta:
        model = Treaty
        fields = ["name", "number"]
        labels = {
            "name": "Название договора",
            "number": "Номер договора",
        }
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введдите название договора",
                }
            ),
            "number": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Введите номер договора"}
            ),
        }


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ["record", "multiplier", 'month']
        labels = {
            "record": "Показание",
            "multiplier": "Тариф (на что будет умножаться)",
            "month": "Месяц показания",
        }
        widgets = {
            "record": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введдите значение показания",
                }
            ),
            "multiplier": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Введите значение тарифа"}
            ),
            "month": MonthSelectorWidget(
                attrs={"class": "form-control", "placeholder": "Введите значение тарифа"}
            ),
        }

