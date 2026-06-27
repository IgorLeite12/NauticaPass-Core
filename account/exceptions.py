from rest_framework import status
from rest_framework.exceptions import APIException, NotFound, ValidationError

from account import messages


class UsingEmailException(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = messages.EMAIL_IN_USING
