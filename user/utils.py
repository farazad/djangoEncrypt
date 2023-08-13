from rest_framework_simplejwt.tokens import AccessToken

class CustomToken(AccessToken):
    def __init__(self, token=None, verify=True):
        super().__init__(token, verify)

    @property
    def payload(self):
        payload = super().payload
        payload['username'] = self.user.username  # Replace 'username' with the field name you want
        return payload