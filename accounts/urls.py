from django.conf.urls import include, url

from accounts.views import account_confirm, account_register

urlpatterns = [


    url(r'account_register/$', account_register, name='account_register'),
    url(r'confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        account_confirm, name='account_confirm'),

]