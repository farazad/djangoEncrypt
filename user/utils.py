from rest_framework_jwt.utils import jwt_payload_handler as default_payload_handler

def jwt_payload_handler(user):
    payload = default_payload_handler(user)
    payload['username'] = user.username
    return payload
