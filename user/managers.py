from django.contrib.auth.models import BaseUserManager

class CustomUsermanager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required!")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("password", True)
        extra_fields.setdefault("phone_number", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        return self.create_user(email, password, phone_number, **extra_fields)