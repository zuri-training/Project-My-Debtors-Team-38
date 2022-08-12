from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
# make logging in case sensitive

User = get_user_model()


class EmailAuthBackend():
    def authenticate(self, request, username, password):
        try:
            user = User.objects.get(email=username)
            success = user.check_password(password)
            print(success)
            if success:
                return user
        except User.DoesNotExist:
            pass
        return None

    def get_user(self, uid):
        try:
            return User.objects.get(pk=uid)
        except:
            return None


class CaseInsensitiveModeBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            case_insensitive_username_field = f'{UserModel.USERNAME_FIELD}__iexact'
            user = UserModel._default_manager.get(
                **{case_insensitive_username_field: username})
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
