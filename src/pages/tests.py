from django.contrib.auth import get_user_model
from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from .models import Subscriber

User = get_user_model()

class SubscriberTestCase(TestCase):
    fixtures = ["subscribers.json", "users.json"]

    def test_valid_subscriber_creation(self):
        email = "test@example.com"
        subscriber = Subscriber.objects.create(email=email)
        self.assertIsNotNone(subscriber)
    
    def test_invalid_subscriber_creation(self):
        with self.assertRaises(ValidationError):
            invalid_entry = "test example"
            validate_email(invalid_entry)
            Subscriber.objects.create(email=invalid_entry)

    def test_unique_email_constraint(self):
        email = "test@example.com"
        Subscriber.objects.create(email=email)
        with self.assertRaises(IntegrityError):
            Subscriber.objects.create(email=email)

    def test_string_representation(self):
        email = "test@example.com"
        subscriber = Subscriber.objects.create(email=email)
        self.assertEqual(str(subscriber), email)

    def test_default_active_status(self):
        email = "test@example.com"
        subscriber = Subscriber.objects.create(email=email)
        self.assertTrue(subscriber.active) 

    def test_susbcribers_exist(self):
        qs = Subscriber.objects.all()
        self.assertTrue(qs.exists())

    def test_users_exist(self):
        qs = User.objects.all()
        self.assertTrue(qs.exists())
