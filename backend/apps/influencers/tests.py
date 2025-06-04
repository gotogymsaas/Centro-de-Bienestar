from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Influencer

class InfluencerMarketingPageTests(SimpleTestCase):
    def test_marketing_page_exists(self):
        response = self.client.get(reverse('influencer_marketing'))
        self.assertEqual(response.status_code, 200)

class InfluencerRegisterTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='user', password='pass')

    def test_login_required(self):
        response = self.client.get(reverse('influencers:register'))
        self.assertEqual(response.status_code, 302)

    def test_create_influencer(self):
        self.client.login(username='user', password='pass')
        response = self.client.post(reverse('influencers:register'), {'code': 'codex', 'commission': '12.00'})
        self.assertRedirects(response, reverse('influencers:dashboard'))
        self.assertTrue(Influencer.objects.filter(user=self.user, code='codex').exists())
