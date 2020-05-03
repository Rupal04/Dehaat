import csv
import logging

from balancesheet.models import BalSheet
from balancesheet.response import SuccessResponse,ErrorResponse
from balancesheet.serializers import BalSheetSerializer
from balancesheet.constants import Success,Error

logger = logging.getLogger(__name__)

def to_dict(obj):
    """Represent instance of a class as dict.
        Arguments:
        obj -- any object
        Return:
        dict
        """

    def serialize(obj):
        """Recursively walk object's hierarchy."""
        if isinstance(obj, (bool, int, float)):
            return obj
        elif isinstance(obj, dict):
            obj = obj.copy()
            for key in obj:
                obj[key] = serialize(obj[key])
            return obj
        elif isinstance(obj, list):
            return [serialize(item) for item in obj]
        elif isinstance(obj, tuple):
            return tuple(serialize([item for item in obj]))
        elif hasattr(obj, '__dict__'):
            return serialize(obj.__dict__)
        else:
            return repr(obj)

    return serialize(obj)


def upload_data_to_database(file_obj):
    try:
        flag = False
        reader = csv.reader(file_obj)
        for row in reader:
            if flag:
                particular1 = row[0]
                y_2015 = row[1]
                y_2016 = row[2]

                particular2 = row[3]
                y2_2015 = row[4]
                y2_2016 = row[5]

                if (particular1 != ' ' and particular1 != '' and particular1 != "Total Rs.") \
                        and y_2015 != ' ' and y_2016 != ' ':

                    BalSheet.objects.create(particular=particular1, year_2015=y_2015, year_2016=y_2016)

                if (particular2 != ' ' and particular2 != '' and particular2 != "Total Rs.") \
                        and y2_2015 != ' ' and y2_2016 != ' ':

                    BalSheet.objects.create(particular=particular2, year_2015=y2_2015, year_2016=y2_2016)
            else:
                flag = True
        return True

    except Exception as e:
        logger.error(Error.EXCEPTION + str(e))
        return None


def get_data(**kwargs):
    try:
        if 'year' in kwargs:
            year = kwargs.get('year')

        if 'var_name' in kwargs:
            var_name = kwargs.get('var_name')

        year_val = "year_" + year
        if var_name and year:
            bal_obj = BalSheet.objects.get(particular=var_name)
            balance = (BalSheetSerializer(bal_obj)).data
            result = "Value of " + var_name + " in " + year + ": " + balance[year_val]
            return SuccessResponse(msg=Success.DATA_FETCH_SUCCESS, results=result)
        else:
            return ErrorResponse(msg=Error.MISSING_DETAILS)

    except Exception as e:
        logger.error(Error.EXCEPTION + str(e))
        return None

