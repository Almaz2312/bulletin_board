from rest_framework.test import APITestCase
from rest_framework.reverse import reverse_lazy
from rest_framework import status
from django.contrib.auth import get_user_model

# Create your tests here.

User = get_user_model()


class RegisterTest(APITestCase):
    def test_POST_register(self):
        data = {'username': 'abcdefg', 'email': 'user@example.com',
                'password': "abc123abc", 'password_confirm': "abc123abc",
                }
        request = self.client.post(reverse_lazy('api_register'), data=data)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        print(User.objects.first())
        user = User.objects.first()
        self.assertEqual(user['username'], 'abcdefg')
