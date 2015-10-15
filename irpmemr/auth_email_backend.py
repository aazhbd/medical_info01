#auth_email_backend.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User


class EmailBackend(ModelBackend):
    """
	Authenticate against django.contrib.auth.models.User
	"""

    def authenticate(self, **credentials):
        return 'username' in credentials and \
        self.authenticate_by_username_or_email(**credentials)

    def authenticate_by_username_or_email(self, username=None, password=None):
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = None
        if user:
            return user if user.check_password(password) else None
        else:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

