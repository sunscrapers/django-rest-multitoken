# Django Rest Multitoken

[![Build Status](https://travis-ci.org/sunscrapers/django-rest-multitoken.svg?branch=master)](https://travis-ci.org/sunscrapers/django-rest-multitoken)
[![Coverage Status](https://coveralls.io/repos/sunscrapers/django-rest-multitoken/badge.png?branch=master)](https://coveralls.io/r/sunscrapers/django-rest-multitoken?branch=master)

Implementation of [Django Rest Framework token authentication](http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication) that maintains multiple tokens for each user.

Currently the project is still under development. It was extracted from [djoser](https://github.com/sunscrapers/djoser) library. Original draft version is [available here](https://github.com/sunscrapers/djoser/tree/custom-auth-token).

Developed by [SUNSCRAPERS](http://sunscrapers.com/) with passion & patience.

## Installation

Use pip:

```
pip install git+https://github.com/sunscrapers/django-rest-multitoken.git
```

## Usage

Add `multitoken` app to `INSTALLED_APPS`:

```
INSTALLED_APPS = (
    'django.contrib.auth',
    (...),
    'rest_framework',
    'multitoken',
    (...),
)
```

Configure `urls.py`:

```
urlpatterns = patterns('',
    (...),
    url(r'^auth/', include('multitoken.urls')),
)
```

Set up Django Rest Framework authentication strategy to `multitoken.authentication.TokenAuthentication`:

```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'multitoken.authentication.TokenAuthentication',
    ),
}
```

## Endpoints

### Login

Use this endpoint to obtain user authentication token.

#### `POST`

URL: `/login/`

* **request**

    * data:

        `{{ User.USERNAME_FIELD }}`

        `password`
        
        `client`

* **response**

    * status: `HTTP_200_OK` (success)

    * data:

        `auth_token`

### Logout

Use this endpoint to logout user and remove user authentication token.

#### `POST`

URL: `/logout/`

* **response**

    * status: `HTTP_200_OK` (success)

## Development

To start developing on **django-rest-multitoken**, clone the repository:

`$ git clone git@github.com:sunscrapers/django-rest-multitoken.git`

In order to run the tests create virtualenv, go to repo directory and then:

`$ pip install -r requirements-test.txt`

`$ cd testproject`

`$ ./manage.py migrate`

`$ ./manage.py test`
