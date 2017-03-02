from django.test import TestCase
from accounts.models import User
from accounts.forms import RegisterForm
# Create your tests here.


class TestSuperUser(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser('thiago', 'oliveiravicente.not@gmail.com', 'logan277')

    def test_create_superuser_is_created(self):
        '''Test if created super user '''
        self.assertTrue(self.user)

    def test_is_superuser(self):
        '''Test if super user is True'''
        self.assertTrue(self.user.is_superuser)

    def test_is_amdmin(self):
        '''Test if super user is admin'''
        self.assertTrue(self.user.is_admin)

    def test_is_active(self):
        '''Test if superuser is active'''
        self.assertTrue(self.user.is_active)

class TestUserProfile(TestCase):

    def setUp(self):
        self.user =  User.objects.create(username='thiago', email='oliveiravicente.net@gmail.com', password='logan277')

    def test_user_profile(self):
        '''All user must have one profile with email_confirmation False on created'''
        self.assertFalse(self.user.profile.email_confirmation)




class TestRegisterForm(TestCase):

    def setUp(self):
        self.form = RegisterForm(data={'username': 'thiago oliveira', 'email': 'oliveiravicente.net@gmail.com'})

    def test_is_valid(self):
        '''test form register user is_valid '''
        self.assertTrue(self.form.is_valid())

    def test_form_save_email_equal(self):
        '''test if email save in form is equal oliveiravicente.net@gmail.com'''
        user =  self.form.save()
        self.assertEquals(user.email, 'oliveiravicente.net@gmail.com')

    def test_form_save_username_equal(self):
        '''test if username  save in form is equal thiago oliveira'''
        user = self.form.save()
        self.assertEquals(user.username, 'thiago oliveira')

    def test_form_save_password_blank(self):
        '''test if password  save blank'''
        user = self.form.save()
        self.assertEquals(user.password, '')

    def test_form_save_user_not_active(self):
        '''test if user is not active'''
        user = self.form.save()
        self.assertFalse(user.is_active)


