from django.contrib.auth import get_user_model
from djet import assertions, restframework, utils
from rest_framework import status
from multitoken import models, views


def create_user(**kwargs):
    data = {
        'username': 'john',
        'password': 'secret',
        'email': 'john@beatles.com',
    }
    data.update(kwargs)
    user = get_user_model().objects.create_user(**data)
    user.raw_password = data['password']
    return user


class LoginViewTest(restframework.APIViewTestCase,
                    assertions.StatusCodeAssertionsMixin,
                    assertions.InstanceAssertionsMixin):
    view_class = views.LoginView

    def test_post_should_login_user(self):
        user = create_user()
        data = {
            'username': user.username,
            'password': user.raw_password,
            'client': 'my-device',
        }
        request = self.factory.post(data=data)

        response = self.view(request)

        self.assert_status_equal(response, status.HTTP_200_OK)
        token = user.auth_tokens.get()
        self.assertEqual(response.data['auth_token'], token.key)
        self.assertEqual(data['client'], token.client)


class LogoutViewTest(restframework.APIViewTestCase,
                     assertions.StatusCodeAssertionsMixin):
    view_class = views.LogoutView

    def test_post_should_logout_logged_in_user(self):
        user = create_user()
        token = models.Token.objects.create(user=user, client='my-device')

        request = self.factory.post(user=user, token=token)
        response = self.view(request)

        self.assert_status_equal(response, status.HTTP_200_OK)
        self.assertEqual(response.data, None)
        with self.assertRaises(models.Token.DoesNotExist):
            utils.refresh(token)

    def test_post_should_deny_logging_out_when_user_not_logged_in(self):
        create_user()

        request = self.factory.post()
        response = self.view(request)

        self.assert_status_equal(response, status.HTTP_401_UNAUTHORIZED)
