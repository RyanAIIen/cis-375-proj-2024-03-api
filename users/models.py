from django.contrib.auth.models import (AbstractUser,
                                        UserManager as DefaultUserManager)


class UserManager(DefaultUserManager):
    # https://github.com/django/django/blob/master/django/contrib/auth/models.py#L137
    pass


class User(AbstractUser):
    # https://github.com/django/django/blob/master/django/contrib/auth/models.py#L335

    objects = UserManager()

    def __str__(self):
        return self.get_full_name() or self.username
