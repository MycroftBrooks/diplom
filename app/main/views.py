from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from main.forms import RegisterUserForm, SupportForm


# Decorator for views that checks that the user is anonymous, redirecting
def anonymous_required(function=None, redirect_url="main"):

    if not redirect_url:
        redirect_url = settings.LOGIN_REDIRECT_URL

    actual_decorator = user_passes_test(
        lambda u: u.is_anonymous, login_url=redirect_url
    )

    if function:
        return actual_decorator(function)
    return actual_decorator


@anonymous_required
def index(request):
    return render(request, 'main/start.html')


@anonymous_required
def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("main")
    else:
        form = RegisterUserForm()
    return render(request, "main/register.html", {"form": form})


@anonymous_required
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main")
        else:
            return render(request, "main/login.html")
    else:
        return render(request, "main/login.html")


@login_required(login_url='hello')
def main(request):
    return render(request, 'main/main.html')

@login_required(login_url='hello')
def logout_user(request):
    logout(request)
    return redirect("hello")


@login_required(login_url='hello')
def support(request):
    if request.method == "POST":
        form = SupportForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            subject = form.cleaned_data.get("subject")
            message = form.cleaned_data.get("message")
            image = form.cleaned_data.get("image")
            template = render_to_string(
                "main/email_template.html",
                {
                    "email": email,
                    "subject": subject,
                    "message": message,
                    "image": image,
                },
            )
            plain_template = strip_tags(template)
            messages.success(
                request, ("Техподдержка ответит вам скоро по этому email: " + email)
            )
            email = EmailMultiAlternatives(
                subject,
                plain_template,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
            )
            email.attach_alternative(template, "text/html")
            email.send()
            return redirect("main")
    else:
        form = SupportForm()
    return render(request, 'main/support.html', {'form': form})
