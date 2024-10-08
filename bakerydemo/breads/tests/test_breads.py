from django.test import TestCase

from bakerydemo.breads.models import BreadType

class TestBreadType(TestCase):
    """
    Test the BreadType model
    """

    @classmethod
    def setUp(cls):
        cls.bread_type = BreadType(title="Test Bread")
        cls.bread_type.save()

    def test_str(self):
        bread_type = BreadType.objects.get(pk=1)
        self.assertEqual(bread_type.title, "Test Bread")
