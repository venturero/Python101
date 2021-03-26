# pip install xlsxwriter
#import is used to import libraries, xlswriter is a library to create&edit an excel file in python.
import xlsxwriter

names = []
surnames = []
ages = []

x = int(input("Number:"))
if(x <= 0):
    x = int(input("Number:"))
else:
    pass
while (x>0):
    name = str(input("What is your name?"))
    names.append(name)
    surname = str(input("What is your surname?"))
    surnames.append(surname)
    age = int(input("What is your age?"))
    print("**************************************************")
    ages.append(age)
    x-=1
print(names)
print(surnames)
print(ages)

workbook = xlsxwriter.Workbook('hello3.xlsx')


worksheet = workbook.add_worksheet()

worksheet.write("A1", "Names")
worksheet.write("B1", "Surnames")
worksheet.write("C1", "Ages")
y = 0
while x ==0:
    worksheet.write("A2", names[y])
    worksheet.write("B2", surnames[y])
    worksheet.write("C2", ages[y])
    y+=1
    x-=1


workbook.close()

