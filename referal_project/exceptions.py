from rest_framework.exceptions import APIException


class WrongDateException(APIException):
    status_code = 400
    default_detail = 'Wrong date'


class CodeExistsException(APIException):
    status_code = 409
    default_detail = 'This code already exists'


class AlreadyReferralException(APIException):
    status_code = 409
    default_detail = 'You are already a referral'


class SelfReferrerException(APIException):
    status_code = 409
    default_detail = "Can't be a referral of yourself"


class AlreadyReferrerException(APIException):
    status_code = 409
    default_detail = "You are already referrer"


class ReferrerExpiredException(APIException):
    status_code = 400
    default_detail = "This referral code is expired"
