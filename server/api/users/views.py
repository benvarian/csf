from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import ChangePasswordSerializer, RequestResetPasswordSerializer, ResetPasswordSerializer
# from django.contrib.auth.password_validation import validate_password
# from django.core.exceptions import ValidationError

import uuid, datetime

@api_view(['PATCH'])
def change_password(request):
    serializer = ChangePasswordSerializer(data=request.data)
    print(serializer, serializer.is_valid())
    if serializer.is_valid():
        serializer.save()
        return Response("Success")

@api_view(['POST'])
def request_reset_password(request):
    user = User.objects.get(email=request.data["email"])
    user.update(reset_token=uuid.uuid4(), reset_time=datetime.datetime.now())
    return Response({ "reset_token": user.reset_token })


# resetToken
# newPassword