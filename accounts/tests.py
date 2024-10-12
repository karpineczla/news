from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

class UsersManagerTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user =  User.objects.create_user(
            username = "testuser",
            email= "testuser@example.com",
            password = "testpass123",
        )
        self.assertEqual(user.username,"testuser")
        self.assertEqual(user.email,"testuser@example.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user =  User.objects.create_superuser(
            username = "testuser",
            email= "testuser@example.com",
            password = "testpass123",
        )
        self.assertEqual(user.username,"testuser")
        self.assertEqual(user.email,"testuser@example.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

class SignUpTests(TestCase):
    def test_url_exists_at_correct_location_signupview(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code,200)

    def test_signup_view_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"registration/signup.html")

    def test_signup_form(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username":"testuser",
                "email":"testemail@example.com",
                "password1":"testpass123",
                "password2":"testpass123",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(),1)
        self.assertEqual(get_user_model().objects.all()[0].username,"testuser")
        self.assertEqual(get_user_model().objects.all()[0].email,"testemail@example.com")
                        

# Create your tests here.
