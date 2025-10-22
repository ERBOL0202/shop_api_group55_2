from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from users.managers import CustomUsermanager
from django.core.cache import cache

# Create your models here.
class ConfirmationCode(models.Model):
    user = models.OneToOneField("CustomUser", on_delete=models.CASCADE, related_name='confirmation_code')
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Код подтверждения для {self.user.email}"

#class ConfirmationCode(models.Model):
    #PREFIX = "confirmation_code"

    #def _get_key(user_id):
        #return f"{ConfirmationCodeService.PREFIX}:{user_id}"
    
    #def set_code(user_id, code, timeout=300):
        #key = ConfirmationCodeService._get_key(user_id)
        #cache.set(key, code, timeout=timeout)

    #def get_code(user_id):
        #key = ConfirmationCodeService._get_key(user_id)
        #return cache.get(key)
    
    #def verify_code(user_id, code):
        #key = ConfirmationCodeService._get_key(user_id)
        #stored_code = cache.get(key)
        #if stored_code and stored_code == code:
            #cache.delete(key) 
            #return True
        #return False

    

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    phone_number = models.CharField()
    birthdate = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUsermanager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [phone_number]

    def __str__(self):
        return self.email or ""