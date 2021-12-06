from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import ShopUserLoginForm, ShopUserProfileEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.forms import ShopUserEditForm
from django.contrib import auth
from django.urls import reverse

from authapp.models import ShopUser


def login(request):
    title = 'вход'
    next_param = request.GET.get('next', '')

    login_form = ShopUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            return HttpResponseRedirect(reverse('main'))

    context = {
        'title': title,
        'login_form': login_form,
        'next': next_param
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def register(request):
    title = 'регистрация'

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            new_user = register_form.save()
            send_verify_email(new_user)
            return HttpResponseRedirect(reverse('auth:login'))

    else:
        register_form = ShopUserRegisterForm()

    context = {
        'title': title,
        'register_form': register_form
    }

    return render(request, 'authapp/register.html', context)


def edit(request):
    title = 'редактирование'

    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        edit_profile_form = ShopUserProfileEditForm(request.POST, instance=request.user.shopuserprofile)

        if edit_form.is_valid() and edit_profile_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))

    else:
        edit_form = ShopUserEditForm(instance=request.user)
        edit_profile_form = ShopUserProfileEditForm(instance=request.user.shopuserprofile)

    context = {
        'title': title,
        'edit_form': edit_form,
        'edit_profile_form': edit_profile_form
    }

    return render(request, 'authapp/edit.html', context)


def verify(request, email, key):
    user = ShopUser.objects.filter(email=email).first()
    if user:
        if user.activate_key == key and not user.is_activate_key_expired():
            user.activate_user()
            auth.login(request, user)
    return render(request, 'authapp/register_result.html')


def send_verify_email(user):
    verify_links = reverse('authapp:verify', args=[user.email, user.activate_key])
    full_link = f'{settings.BASE_URL}{verify_links}'

    massage = f'Your activation url: {full_link}'

    return send_mail(
                    'Account activation',
                    massage,
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    fail_silently=False
    )
