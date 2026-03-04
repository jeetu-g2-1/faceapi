import hashlib
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from api1.models import APIKey
from django.contrib.auth.models import User

class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get("X-API-KEY")

        if not api_key:
            # No key provided → Forbidden
            raise AuthenticationFailed(detail={"message": "Forbidden"}, code=403)

        # Hash the incoming API key
        hashed_key = hashlib.sha256(api_key.encode()).hexdigest()

        try:
            # Try to find a matching active hashed key
            APIKey.objects.get(hashed_key=hashed_key, is_active=True)
        except APIKey.DoesNotExist:
            # Fetch the stored hashed key for Faceapi
            try:
                key_obj = APIKey.objects.get(name='Faceapi')
                stored_hashed_key = key_obj.hashed_key
            except APIKey.DoesNotExist:
                stored_hashed_key = None

            # Determine debug message
            if hashed_key == stored_hashed_key:
                debug_msg = "Hashed key matches Faceapi key but it is inactive"
            else:
                debug_msg = "Hashed key does not match Faceapi key"

            # Raise Forbidden with debug info
            raise AuthenticationFailed(detail={
                "message": "Forbidden",  # this triggers Moodle check
                "debug": debug_msg,
                "sent_hashed_key": hashed_key,
                "stored_hashed_key": stored_hashed_key
            }, code=403)

        # If API key is valid, return service user
        try:
            user = User.objects.get(username='faceapi_service')
        except User.DoesNotExist:
            raise AuthenticationFailed(detail={
                "message": "Forbidden",
                "debug": "Service user not found"
            }, code=403)

        return (user, None)
