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

for item in range(len(names)):
    worksheet.write(item+1, 0, names[item])
    worksheet.write(item+1, 1, surnames[item])
    worksheet.write(item + 1, 2, ages[item])
"""
for item in range(len(names)):
    worksheet.write(item+1, 0, names[item])
for item in range(len(surnames)):
    worksheet.write(item+1, 1, surnames[item])
for item in range(len(ages)):
    worksheet.write(item+1, 2, ages[item])"""
"""y = 0
z=2
while x ==y:
    worksheet.write("A{}".format(z), names[y])
    worksheet.write("B2{}".format(z), surnames[y])
    worksheet.write("C2{}".format(z), ages[y])
    print(y)
    y+=1
"""

workbook.close()

