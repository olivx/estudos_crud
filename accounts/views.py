from django.contrib.auth import login as django_login, authenticate
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.contrib.sites.shortcuts import get_current_site

from accounts.models import User
from accounts.tokens import account_token_generator
from accounts.forms import RegisterForm, AuthenticanUserForm


def account_register(request):
    form = RegisterForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Active your Books.com Account'
            context = {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_token_generator.make_token(user)
            }

            message = render_to_string(template_name='email_confirmation_books_account.txt',
                                       context=context)

            user.email_user(subject, message=message)
            return render(request, 'thanks.html', {'email_confirmation': user.profile.email_confirmation})

    return render(request, 'register.html', {'form': form})


def account_confirm(request, uidb64, token):
    pk = urlsafe_base64_decode(force_text(uidb64))
    user = get_object_or_404(User, pk=pk)

    if user is not None and account_token_generator.check_token(user, token):
        user.profile.email_confirmation = True
        user.is_active = True
        user.save()

        login(request, user)
        context = {'email_confirmation': user.profile.email_confirmation}
        return render(request, 'thanks.html', context)

    else:
        return render(request, 'invalid_token.hmtl')


def login(request, template_name='registration/login.html'):
    if request.POST:
        form = AuthenticanUserForm(request.POST)
        form.is_valid()
        user = authenticate(email=request.POST['email'], password=request.POST['password'])
        print(user)
        if user is not None:
            if user.is_active and user.profile.email_confirmation:
                django_login(request, user)
                return render(request, 'index.html')

    else:
        form = AuthenticanUserForm()
    return render(request, template_name, {'form': form})
