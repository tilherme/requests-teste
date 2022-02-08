
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError(_('Users must have an email'))

        user = self.model(
            email=email,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )

        user.is_admin = True
        user.save(using=self._db)

        return user
class Address(models.Model):
    city = models.CharField(max_length=255, blank=False, null=False)
    state = models.CharField(max_length=255, blank=False, null=False)
    cep = models.CharField(max_length=255, blank=False, null=False)
    number = models.IntegerField(blank=False, null=False)
    neighborhood = models.CharField(max_length=255, blank=False, null=False)
    street = models.CharField(max_length=255, blank=False,null=False)

    def __str__(self):
        return self.city

class User(AbstractBaseUser):
    username = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, blank=True, null=False)
    profile_image = models.ImageField(upload_to='profile-image/',null=True, blank=True)
    phone = models.CharField(max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
