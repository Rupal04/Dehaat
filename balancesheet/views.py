# -*- coding: utf-8 -*-

import logging

from tabula import read_pdf

from rest_framework.decorators import api_view
from balancesheet.utility import upload_data_to_database, get_data, to_dict, create_csv
from rest_framework.response import Response
from rest_framework import status
from balancesheet.response import ErrorResponse, ServerErrorResponse, SuccessResponse
from balancesheet.constants import Success, Error

logger = logging.getLogger(__name__)


@api_view(['POST'])
def convert_pdf_to_csv(request):
    try:
        data = request.data
        path = data.get('path', None)
        if path:
            df = read_pdf(path)

            # convert dataframe to ndarray
            arr = df[0].to_numpy()

            is_created = create_csv(arr)

            if is_created:
                response = SuccessResponse(msg=Success.SHEET_CONVERT_SUCCESS)
                return Response(to_dict(response), status=status.HTTP_200_OK)
            else:
                response = ErrorResponse(msg=Error.SHEET_CONVERT_ERROR)
                return Response(to_dict(response), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            response = ErrorResponse(msg=Error.PATH_NOT_PROVIDED)
            return Response(to_dict(response), status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        logger.error(Error.EXCEPTION + str(e))
        response = ServerErrorResponse()
        return Response(to_dict(response), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def upload_csv(request):
    try:
        data = request.data
        path = data.get('path', None)
        if path:
            with open(path, "rt") as file_obj:
                is_uploaded = upload_data_to_database(file_obj)

            if is_uploaded:
                response = SuccessResponse(msg=Success.UPLOAD_SHEET_SUCCESS)
                return Response(to_dict(response), status=status.HTTP_200_OK)
            else:
                response = ErrorResponse(msg=Error.UPLOAD_SHEET_ERROR)
                return Response(to_dict(response), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            response = ErrorResponse(msg=Error.PATH_NOT_PROVIDED)
            return Response(to_dict(response), status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        logger.error(Error.EXCEPTION + str(e))
        response = ServerErrorResponse()
        return Response(to_dict(response), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_variable_data(request):
    try:
        var_name = request.query_params.get('var_name', None)
        year = request.query_params.get('year', None)

        response = get_data(**{"var_name": var_name, "year": year})

        if not response:
            response = ErrorResponse(msg=Error.DATA_FETCH_ERROR)
            return Response(to_dict(response), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if response and response.success is False:
            return Response(to_dict(response), status=status.HTTP_400_BAD_REQUEST)

        return Response(to_dict(response), status=status.HTTP_200_OK)

    except Exception as e:
        logger.error(Error.EXCEPTION + str(e))
        response = ServerErrorResponse()
        return Response(to_dict(response), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
