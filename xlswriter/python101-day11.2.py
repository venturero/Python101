import xlsxwriter

workbook = xlsxwriter.Workbook("hello2.xlsx")
worksheet = workbook.add_worksheet("to_delete")

succes2 = workbook.add_format(
    {
        "bg_color":"#FF0000",
        "font":"Calibri",
        "font_size":11,
        "bold":True
    }
)

worksheet.write("E1", "Models6764")
worksheet.write("E2", "Models32423")
worksheet.write("E3", "Model3243432s")

options = {
    'delete_columns':        True,
    'delete_rows':           False,
}

my_dict = {"x": [3, 4, 5],
           "y": [5, 12, 13],
           "z": [8, 15, 17]}
col_num = 0
for key, value in my_dict.items():
    worksheet.write(0, col_num, key, succes2)
    worksheet.write_column(1, col_num, value)
    col_num += 1

worksheet.protect('E', {"delete_columns": True})


cell_format = workbook.add_format({'bold': True})
worksheet.set_default_row(hide_unused_rows=True)#to hide unused rows
worksheet.set_column('E:E', 20,  cell_format, {'hidden': 1})#to hide columns

workbook.close()

#worksheet.set_column(4, 20, cell_format, {'hidden': True})
