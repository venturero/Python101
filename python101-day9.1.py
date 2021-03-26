#import is used to import libraries, xlswriter is a library to create&edit an excel file in python.
import xlsxwriter

workbook = xlsxwriter.Workbook('hello2.xlsx')


worksheet = workbook.add_worksheet()


worksheet.write("A1", "First Try..")
worksheet.write("B1", "Second")
worksheet.write("C1", "Third")
worksheet.write("D1", "Enough")


workbook.close()