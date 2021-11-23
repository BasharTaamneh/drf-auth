from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Electro


class ElectroModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(
        username='tester', password='pass')
        test_user.save()

        test_Electro = Electro.objects.create(
            owner=test_user,
            elctronic_name='Title of Electro',
            description='Words about the Electro',
            rating = 10,
        )
        test_Electro.save()

    def test_blog_content(self):
        electro = Electro.objects.get(id=1)

        self.assertEqual(str(electro.owner), 'tester')
        self.assertEqual(electro.elctronic_name, 'Title of Electro')
        self.assertEqual(electro.description, 'Words about the Electro')
        self.assertEqual(electro.rating, 10)
