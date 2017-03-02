from django.conf.urls import url
from django.contrib import admin

from django.contrib.auth.views import login, logout
from django.views.generic import TemplateView
from core.views import book_list, book_save, book_update, book_delete, book_search
from accounts.views import account_register , account_confirm

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # url home view
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),

    # url login logout
    url(r'^login/$', login, name='login', kwargs={'template_name': 'partial/login.html'}),
    url(r'^logout/$', logout, name='logout', kwargs={'template_name': 'partial/logout.html'}),

    # actions views
    url(r'^book/list/$', book_list, name='book_list'),
    url(r'^book/book_save/$', book_save, name='book_save'),
    url(r'^book/book_search/$', book_search, name='book_search'),
    url(r'^book/book_update/(?P<pk>[\d]+)$', book_update, name='book_update'),
    url(r'^book/book_delete/(?P<pk>[\d]+)$', book_delete, name='book_delete'),


    # actions accounts
    url(r'^account/account_register/$', account_register, name='account_register'),
    url(r'^account/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        account_confirm, name='account_confirm'),

    url(r'^contact/$', book_list, name='contact'),

]
