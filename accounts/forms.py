from django import forms
from django.contrib.auth import authenticate

from accounts.models import User
from django.utils.translation import ugettext_lazy as _


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(max_length=30, widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(max_length=30, widget=forms.PasswordInput, required=True)

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(_("The two password fields didn't match."))
        return self.cleaned_data

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class AuthenticanUserForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=30, required=True)
    password = forms.CharField(label='Password', max_length=30, required=True, widget=forms.PasswordInput)

    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(email)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
        'email_confirmation': _(
            'this email is not confirmed yet, please confirm the your eamil and try again'
        ),
    }

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user = authenticate(email=email, password=password)
            if self.user is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'email': 'Email'},
                )

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        """
        Controls whether the given User may log in. This is a policy setting,
        independent of end-user authentication. This default behavior is to
        allow login by active users, and reject login by inactive users.

        If the given user cannot log in, this method should raise a
        ``forms.ValidationError``.

        If the given user may log in, this method should return None.
        """
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )

        if not user.profile.email_confirmation:
            raise forms.ValidationError(
                self.error_messages['email_confirmation'],
                code='email_confirmation'
            )

    class Meta:
        fields = ('email', 'password')
