DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

INSTALLED_APPS = (
    'bootstrap3',
)

BOOTSTRAP3 = {
    'javascript_in_head': True,
    'form_required_class': 'bootstrap3-req',
}

SECRET_KEY = 'bootstrap3isawesome'
