from tabula import read_pdf
import csv
import itertools

output_path ="/Users/rupalgupta/Downloads/Dehaat/BalSheet.csv"


def create_csv(data):
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


def pdf_to_csv():
    pdf_path = "/Users/rupalgupta/Downloads/Dehaat/BalSheet.pdf"
    df = read_pdf(pdf_path)
    arr=df[0].to_numpy()
    create_csv(arr)


if __name__=="__main__":
    pdf_to_csv()
