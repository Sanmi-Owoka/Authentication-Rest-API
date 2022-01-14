from rest_framework import generics, status
from ..models import User
from ..serializers import PasswordResetSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response


class PasswordResetView(generics.GenericAPIView):
    serializer_class = PasswordResetSerializer

    def put(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        otp = serializer.data.get('otp')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')
        try:
            user = User.objects.get(email=email)
        except ObjectDoesNotExist:
            return Response(data={"Invalid Operation": "User does not exist"}, status=404)
        if password == confirm_password:
            keygen = user.otp
            OTP = keygen
            if otp != OTP:
                return Response(data={
                    "Invalid Operation": "Failure due to otp expiration",
                    "errors": {
                        'otp_code': "Does not match or expired",
                    }
                }, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(password)
            user.save()
            return Response(data={
                "Success": "You've successfully Reset your password",
            }, status=status.HTTP_200_OK)
        else:
            return Response(data={"Invalid credentials": "Error when entering credentials", "errors": {
                "passwords": "The two Passwords must be the same"
            }}, status=status.HTTP_400_BAD_REQUEST)
