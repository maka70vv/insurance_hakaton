from rest_framework import serializers

from .models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        field = (
            "date_of_birth",
            "passport_number",
            "date_of_issue",
            "date_expiration",
            "authority",
            "sex",
            "place_of_birth",
            "place_of_residence",
            "residental_addres",
        )


class UserSerializer(serializers.HyperLinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        field = (
            "first_name",
            "last_name",
            "email",
            "password",
            "iin",
            "iban",
            "profile",
        )
        extra_kwarg = {"password": {"write_only": True}}

    def create(self, validated_data):
        profile_data = validated_data.pop("profile")
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop("profile")
        profile = instance.profile

        instance.iin = validated_data.get("iin", instance.iin)
        instance.iban = validated_data.get("iban", instance.iban)
        instance.save()

        profile.date_of_birth = profile_data.get(
            "date_of_birth",
            profile.date_of_birth,
        )
        profile.passport_number = profile_data.get(
            "passport_number",
            profile.passport_number,
        )
        profile.date_of_issue = profile_data(
            "date_of_issue",
            profile.date_of_issue,
        )
        profile.date_expiration = profile_data(
            "date_expiration",
            profile.date_expiration,
        )
        profile.authority = profile_data("authority", profile.authority)
        profile.sex = profile_data("sex", profile.sex)
        profile.place_of_birth = profile_data(
            "place_of_birth",
            profile.place_of_birth,
        )
        profile.place_of_residence = profile_data(
            "place_of_residence",
            profile.place_of_residence,
        )
        profile.residental_addres = profile_data(
            "residental_addres",
            profile.residental_addres,
        )
        profile.photo = profile_data.get("photo", profile.photo)
        profile.save()
