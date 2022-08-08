from django.forms import ModelForm
from django.contrib.auth import get_user_model, forms
from django.core.exceptions import ValidationError
from .models import SchoolProfile, Student, GuardianProfile, GuardianChild, School, Guardian, User

from django import forms as d_forms
# from allauth.account.forms import SignupForm

# User = get_user_model()


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class SchoolRegistrationForm(forms.UserCreationForm):

    error_message = forms.UserCreationForm.error_messages.update(
        {
            "duplicate_email": ("This email has already been taken.")
        }
    )

    class Meta:
        model = School
        fields = ("email",)
        # field_classes = {"email": UsernameField}

    def clean_email(self):
        email = self.cleaned_data["email"].lower()

        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email

        raise ValidationError(
            self.error_messages["duplicate_email"]
        )


class GuardianRegistrationForm(forms.UserCreationForm):

    error_message = forms.UserCreationForm.error_messages.update(
        {
            "duplicate_email": (
                "This email has already been taken."
            )
        }
    )

    class Meta:
        model = Guardian
        fields = ("email",)
        # field_classes = {"email": UsernameField}

    def clean_email(self):
        email = self.cleaned_data["email"].lower()

        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email

        raise ValidationError(
            self.error_messages["duplicate_email"]
        )


class SchoolProfileForm(ModelForm):
    class Meta:
        model = SchoolProfile
        fields = '__all__'
        exclude = ['school', ]


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['school', ]


class GuardianProfileForm(ModelForm):
    class Meta:
        model = GuardianProfile
        fields = '__all__'
        exclude = ['guardian', ]


class GuardianChildForm(ModelForm):
    class Meta:
        model = GuardianChild
        fields = '__all__'
        exclude = ['guardian', ]
