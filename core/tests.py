from accounts.models import User
from django.test import TestCase

from django.shortcuts import resolve_url as r

from core.models import Books


# Create your tests here.

class TestHome(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('home'))

    def test_home(self):
        '''Test Get home '''
        self.assertEquals(self.resp.status_code, 200)

    def test_template_home(self):
        '''Home must user template index.html'''
        self.assertTemplateUsed('index.html')


class TestBooksViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='thiago', email='oliveiravicente.net@gmail.com',password='logan277')

        self.client.login(email='oliveiravicente.net@gmail.com', password='logan277')
        self.resp = self.client.get(r('book_list'))

    def test_get_book_list(self):
        '''Get on book_list page '''
        self.assertEquals(200, self.resp.status_code)

    def test_html_used_books(self):
        '''Templete  books.html must be used '''
        self.assertTemplateUsed('books.html')




class TestBooksModels(TestCase):
    def setUp(self):
        '''Setup Model Books '''
        self.book = Books.objects.create(author='thiago oliveira', title='python is the best',
                                         description='this is a short descrition for boon on test',
                                         pages=25, price=20.63, visible=True, type_book=Books.EBOOK)

    def test_create_book(self):
        '''Simple Test to Create Object Book '''
        self.assertTrue(Books.objects.exists())

    def test_description_can_be_blank(self):
        '''In Model Book description can be blank'''
        field = self.book._meta.get_field('description')
        self.assertTrue(field.blank)

    def test_published_can_be_blank(self):
        '''In Model Book Publised can be Blank '''
        field = self.book._meta.get_field('published')
        self.assertTrue(field.blank)

    def test_visible_true(self):
        '''Test if visible True  '''
        self.assertTrue(self.book.visible)
