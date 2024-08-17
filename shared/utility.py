import re
from rest_framework.exceptions import ValidationError

email_regex = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b")
phone_regex = re.compile(r"(\+[0-9]+\s*)?(\([0-9]+\))?[\s0-9\-]+[0-9]+")


def check_email_or_phone(email_or_phone):
    if re.fullmatch(email_regex, email_or_phone):
        email_or_phone = 'email'
    
    elif re.fullmatch(phone_regex, email_or_phone):
        email_or_phone = 'phone'

    else:
        data = {
            "success" : False,
            "message" : "Email yoki telefon nomer kiriting"
        }
        raise ValidationError(data)
    
    return email_or_phone