from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth.views import logout
from django.views.generic import TemplateView
from core.views import book_list, book_save, book_update, book_delete, book_search
from accounts.views import login
urlpatterns = [

    # admin
    url(r'^admin/', admin.site.urls),

    # actions accounts
    url(r'^account/', include('accounts.urls')),


    # url home view
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),

    # url login logout
    url(r'^login/$', login, name='login'),
    # url(r'^login/$', login, name='login', kwargs={'template_name': 'partial/login.html'}),
    url(r'^logout/$', logout, name='logout', kwargs={'template_name': 'registration/logout.html'}),

    # actions views
    url(r'^book/list/$', book_list, name='book_list'),
    url(r'^book/book_save/$', book_save, name='book_save'),
    url(r'^book/book_search/$', book_search, name='book_search'),
    url(r'^book/book_update/(?P<pk>[\d]+)$', book_update, name='book_update'),
    url(r'^book/book_delete/(?P<pk>[\d]+)$', book_delete, name='book_delete'),




    url(r'^contact/$', book_list, name='contact'),

]
