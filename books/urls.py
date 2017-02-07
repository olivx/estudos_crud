"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

from django.contrib.auth.views import login, logout
from django.views.generic import TemplateView
from core.views import book_list, book_save, book_update, book_delete, book_search

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

    url(r'^contact/$', book_list, name='contact'),

]
