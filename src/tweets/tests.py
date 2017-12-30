from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.
from .models import Tweet

User = get_user_model()


class TweetModelTestCase(TestCase):
    def setUp(self):
        example_user = User.objects.create(
            username= 'John123',
            title='Random Title',
            text='Random text',
        )

    def test_tweet_item(self):
        obj = Tweet.objects.create(
                    user= User.objects.first(),
                    title='Random Title',
                    text='Random text',
                )
        self.assertTrue(obj.title == 'Random Title')
        self.assertTrue(obj.text == 'Random text')
        self.assertEqual(obj.id, 1)
        absolute_url = reverse('tweet:detail', kwargs={"pk": 1})
        self.assertEqual(obj.get_absolute_url(), absolute_url)

    def test_tweet_url(self):
        obj = Tweet.objects.create(
            user=User.objects.first(),
            title='Random Title',
            text='Random text',
        )
        absolute_url = reverse('tweet:detail', kwargs={"pk": obj.pk})
        self.assertEqual(obj.id, 2)
