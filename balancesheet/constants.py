class Success(object):
    SUCCESS_RESPONSE = "Successful"

    DATA_FETCH_SUCCESS = "Successfully fetched data."

    SHEET_CONVERT_SUCCESS = "Successfully converted sheet from pdf to csv."

    UPLOAD_SHEET_SUCCESS = "Successfully uploaded sheet."


class Error(object):
    ERROR_RESPONSE = "Error"
    SERVER_ERROR_5XX = "SERVER ERROR"

    EXCEPTION = "Some Unexpected error occurred. Error is : "
    MISSING_DETAILS = "Some of the input details are missing."

    SHEET_CONVERT_ERROR = "Error in converting sheet."

    PATH_NOT_PROVIDED = "Path for the uploading sheet is not provided."
    UPLOAD_SHEET_ERROR = "Error occurred while uploading a balance sheet."
    UPLOAD_SHEET_SUCCESS = "Successfully uploaded balance sheet."

    DATA_FETCH_ERROR = "Error in fetching data"
