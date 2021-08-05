from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from django.conf import settings
from rest_framework import status


def ok(data=None, result=1, message_code='Successfully'):
    message = message_code
    headers = {
        'X-mtrapp-alert': None
    }
    data_response = {
        "result": result,
        "message": message,
        "data": data
    }
    # logging.info(data_response)

    return Response(data=data_response, status=status.HTTP_200_OK, headers=headers)


def bad_request(data=None, result=-1, message_code='Fail!'):
    message = message_code
    headers = {
        'X-mtrapp-alert': None
    }
    data_response = {
        "result": result,
        "message": message,
        "data": data
    }
    # logging.info(data_response)

    return Response(data=data_response, status=status.HTTP_400_BAD_REQUEST, headers=headers)
