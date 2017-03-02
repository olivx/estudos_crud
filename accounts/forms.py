from django import forms
from accounts.models import User
from django.utils.translation import ugettext_lazy as _


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(max_length=30, widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(max_length=30, widget=forms.PasswordInput, required=True)

    def clean(self):
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
