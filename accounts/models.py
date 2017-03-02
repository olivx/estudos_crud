from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser


# Create your models here.
class UserManager(BaseUserManager):
    """
    Custon user manager
    """

    def _create_user(self, username, email, password, **kwargs):

        if not email:
            raise ValueError(_('The e-mail must be set'))
        if not username:
            raise ValueError(_('The User Name must be set'))

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        kwargs.setdefault('is_admin', False)
        return self._create_user(username, email, password, kwargs)

    def create_superuser(self, username, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_admin', True)
        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if kwargs.get('is_admin') is not True:
            raise ValueError('Superuser must have is_admin=True')
        return self._create_user(username, email, password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    """"    Custom user class    """
    email = models.EmailField(_('Email'), unique=True, db_index=True)
    username = models.CharField(_('User Name'), max_length=150)
    last_name = models.CharField(_('Last Name'), max_length=150, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return '%s %s' % (self.username, self.last_name)

    def get_short_name(self):
        return self.username

    def email_user(self, subject, message):
        '''send email to user tis account'''
        send_mail(subject=subject, message=message,
                  from_email=settings.EMAIL_HOST_USER, recipient_list=[self.email])


class Profile(models.Model):
    """     Profile user    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="profile")
    email_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return str(self.email_confirmation)

@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

