class Success(object):
    SUCCESS_RESPONSE = "Successful"

    DATA_FETCH_SUCCESS = "Successfully fetched data."


class Error(object):
    ERROR_RESPONSE = "Error"
    SERVER_ERROR_5XX = "SERVER ERROR"

    EXCEPTION = "Some Unexcepted error occurred. Error is : "
    MISSING_DETAILS = "Some of the input details are missing."

    PATH_NOT_PROVIDED = "Path for the uploading sheet is not provided."
    UPLOAD_SHEET_ERROR = "Error occurred while uploading a balance sheet."
    UPLOAD_SHEET_SUCCESS = "Successfully uploaded balance sheet."

    DATA_FETCH_ERROR = "Error in fetching data"
