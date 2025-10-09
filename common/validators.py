from datetime import date
from rest_framework.exceptions import ValidationError

def validate_user_age_from_token(birthdate_str):
    if not birthdate_str:
        raise ValidationError("Укажите дату рождения, чтобы создать продукт.")

    try:
        birthdate = date.fromisoformat(birthdate_str)
    except ValueError:
        raise ValidationError("Некорректная дата рождения в токене.")

    today = date.today()
    age = today.year - birthdate.year - (
        (today.month, today.day) < (birthdate.month, birthdate.day)
    )

    if age < 18:
        raise ValidationError("Вам должно быть 18 лет, чтобы создать продукт.")