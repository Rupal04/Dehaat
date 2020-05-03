import csv
import logging
import itertools

from balancesheet.models import BalSheet
from balancesheet.response import SuccessResponse,ErrorResponse
from balancesheet.serializers import BalSheetSerializer
from balancesheet.constants import Success,Error

logger = logging.getLogger(__name__)

output_path = "/Users/rupalgupta/Downloads/Dehaat/BalSheet.csv"

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


def create_csv(data):
    try:
        data_csv = open(output_path, 'w')
        writer = csv.writer(data_csv, dialect='excel')

        header_names=[]
        headers=data[0]
        for head in headers:
            header_names.append(head)
        writer.writerow(header_names)

        column1_data=data[1][0]
        column1=column1_data.splitlines()

        column2_data=data[1][1]
        column2=column2_data.splitlines()
        column2.append(data[2][1])

        left_col2_vals=data[3][1]
        left_col2=left_col2_vals.splitlines()
        for vals in left_col2:
            column2.append(vals)

        column3_data=data[1][2]
        column3=column3_data.splitlines()
        column3.append(data[2][2])

        left_col3_vals=data[3][2]
        left_col3=left_col3_vals.splitlines()
        for vals in left_col3:
            column3.append(vals)

        column4_data = data[1][3]
        column4 = column4_data.splitlines()

        column5_data=data[1][4]
        column5=column5_data.splitlines()
        column5.append(data[2][3])

        left_col5_vals=data[3][3]
        left_col5 = left_col5_vals.splitlines()
        for vals in left_col5:
            column5.append(vals)

        column6_data = data[1][5]
        column6 = column6_data.splitlines()
        column6.append(data[2][4])

        left_col6_vals = data[3][4]
        left_col6 = left_col6_vals.splitlines()
        for vals in left_col6:
            column6.append(vals)

        final_data_rows = [list(e) for e in itertools.zip_longest(column1, column2, column3, column4, column5, column6, fillvalue=" ")]

        for data_rows in final_data_rows:
            writer.writerow(data_rows)

        total=data[4]
        total_row=[]
        for val in total:
            total_row.append(val)
        writer.writerow(total_row)
        data_csv.close()
        return True

    except Exception as e:
        logger.error(Error.EXCEPTION + str(e))
        return None


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
                        and y_2015 != ' ' and y_2016 != ' ' and not BalSheet.objects.filter(
                        particular=particular1, year_2015=y_2015, year_2016=y_2016).exists():

                        BalSheet.objects.create(particular=particular1, year_2015=y_2015, year_2016=y_2016)

                if (particular2 != ' ' and particular2 != '' and particular2 != "Total Rs.") \
                        and y2_2015 != ' ' and y2_2016 != ' ' and not BalSheet.objects.filter(
                        particular=particular2, year_2015=y2_2015, year_2016=y2_2016).exists():

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

