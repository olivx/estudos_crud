from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


class AccountTokenGenarator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.profile.email_confirmation)
        )


account_token_generator = AccountTokenGenarator()
