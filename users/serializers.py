from .models import(
    UserModel, UserConfirmation, VIA_EMAIL, VIA_PHONE, NEW, CODE_VERIFIED, DONE, PHOTO_STEP
)
from rest_framework import exceptions, serializers
from django.db.models import Q
from rest_framework.exceptions import ValidationError
from shared.utility import check_email_or_phone


class SignUpSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    email_phone_number = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = (
            'id',
            'auth_type',
            'auth_status',
            'email_phone_number',  # Добавляем в список fields
        )

        extra_kwargs = {
            'auth_type': {'read_only': True},
            'auth_status': {'read_only': True},
        }

    def validate(self, data):
        data = super(SignUpSerializer, self).validate(data)
        user_input = data.pop('email_phone_number', None)

        if user_input:
            input_type = check_email_or_phone(user_input.lower())
            if input_type == 'email':
                data['auth_type'] = VIA_EMAIL
            elif input_type == 'phone':
                data['auth_type'] = VIA_PHONE
            else:
                raise ValidationError("Invalid input: must be a valid email or phone number.")

        return data

    def create(self, validated_data):
        return super(SignUpSerializer, self).create(validated_data)


 
