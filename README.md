# Django Rest Multitoken

[![Build Status](https://travis-ci.org/sunscrapers/django-rest-multitoken.svg?branch=master)](https://travis-ci.org/sunscrapers/django-rest-multitoken)
[![Coverage Status](https://coveralls.io/repos/sunscrapers/django-rest-multitoken/badge.png?branch=master)](https://coveralls.io/r/sunscrapers/django-rest-multitoken?branch=master)

Implementation of [Django Rest Framework token authentication](http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication) that maintains multiple tokens for each user.

Currently the project is under heavy development. It was extracted from [djoser](https://github.com/sunscrapers/djoser) library. Working version is [available here](https://github.com/sunscrapers/djoser/tree/custom-auth-token).


## Development

To start developing on **django-rest-multitoken**, clone the repository:

`$ git clone git@github.com:sunscrapers/django-rest-multitoken.git`

In order to run the tests create virtualenv, go to repo directory and then:

`$ pip install -r requirements-test.txt`

`$ cd testproject`

`$ ./manage.py migrate`

`$ ./manage.py test`
