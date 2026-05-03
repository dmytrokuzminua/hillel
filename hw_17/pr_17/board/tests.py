from django.test import TestCase
from .models import Ad, Category
from django.contrib.auth.models import User


class AdModelTest(TestCase):

    def test_price_validation(self):
        user = User.objects.create(username="test")
        category = Category.objects.create(name="Test", description="desc")

        ad = Ad(
            title="Test",
            description="desc",
            price=-10,
            user=user,
            category=category
        )

        with self.assertRaises(Exception):
            ad.full_clean()