from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from companies.models import Company


def has_valid_password(password, confirm_password):
    return password is not None and len(password) > 0 and password == confirm_password


class CompanySerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    nit = serializers.CharField()
    address = serializers.CharField()
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Company
        fields = ('nit', 'name', 'address',
                  'confirm_password', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        confirm_password = validated_data.pop('confirm_password', None)
        if not has_valid_password(password, confirm_password):
            raise ValidationError('The password did not match with the confirm password field')
        company = Company.objects.create(**validated_data, is_active=True, is_superuser=True, is_staff=True)
        company.set_password(password)
        company.save()
        return company

