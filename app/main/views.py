from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from main.forms import RegisterUserForm, SupportForm, TreatyForm, RecordForm
from main.models import Treaty, Record


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


@login_required(login_url='hello')
def support(request):
    if request.method == "POST":
        form = SupportForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            subject = form.cleaned_data.get("subject")
            message = form.cleaned_data.get("message")
            template = render_to_string(
                "main/email_template.html",
                {
                    "email": email,
                    "subject": subject,
                    "message": message,
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


@login_required(login_url='hello')
def main(request):
    treaties = Treaty.objects.filter(user_id=request.user.id)
    return render(request, 'main/main.html', {'treaties': treaties})


@login_required(login_url='hello')
def delete_treaty(request, id):
    treaty = Treaty.objects.filter(id=id)
    number = treaty.values()[0]['number']
    treaty.delete()
    messages.info(
        request,
        f"Удален договор с номером {number}",
    )
    return redirect('main')


@login_required(login_url='hello')
def create_treaty(request):
    submitted = False
    if request.method == "POST":
        form = TreatyForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(
                request,
                f"Создан договор с номером {obj.number}",
            )
            return redirect("main")
    else:
        form = TreatyForm
        if "submitted" in request.GET:
            submitted = True
    return render(request, "main/create_treaty.html", {"form": form, "submitted": submitted})


@login_required(login_url='hello')
def detail_treaty(request, id):
    records = Record.objects.filter(treaty_id=id).order_by('month')
    labels_data = []
    data_record = []
    data_payment = []

    for i, obj in enumerate(records):
        labels_data.append(obj.month)
        data_record.append(obj.record)
        if i > 0:
            data_payment.append((obj.record - records[i-1].record) * obj.multiplier)

    return render(
        request,
        'main/treaty.html',
        {
            'treaty': Treaty.objects.get(id=id),
            'records': records,
            'labels_data': labels_data,
            'data_record': data_record,
            'data_payment': data_payment,
        }
    )


@login_required(login_url='hello')
def delete_record(request, id):
    record = Record.objects.filter(id=id)
    treaty_id = record.values()[0]['treaty_id']
    record.delete()
    messages.info(
        request,
        f"Удалено показание!",
    )
    return redirect(f'/treaty/{treaty_id}')


@login_required(login_url='hello')
def create_record(request, id):
    submitted = False
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.treaty_id = id
            obj.save()
            messages.success(
                request,
                f"Сохранено показание",
            )
            return redirect(f"/treaty/{id}")
    else:
        form = RecordForm
        if "submitted" in request.GET:
            submitted = True
    return render(request, "main/create_treaty.html", {"form": form, "submitted": submitted})


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
def logout_user(request):
    logout(request)
    return redirect("hello")
