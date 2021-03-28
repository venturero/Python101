import xlsxwriter

cars =[]
brands = []
models = []
colors = []
ages = []
prices = []

x = int(input("How many cars do you have?"))

while(x>0):
    brand = str(input("Brand:"))
    brands.append(brand)
    model = str(input("Model:"))
    models.append(model)
    color = str(input("Color:"))
    colors.append(color)
    age = int(input("Age:"))
    ages.append(age)
    price = int(input("Price:"))
    prices.append(price)
    print("*********************")
    x -= 1
print(brands)
print(models)
print(colors)
print(ages)
print(prices)

#cars.append(brands,models,colors,ages,prices)

workbook = xlsxwriter.Workbook("cars3.xlsx")
worksheet = workbook.add_worksheet()

worksheet.write("A1", "Brands",)#cell_format
worksheet.write("B1", "Models")
worksheet.write("C1", "Ages")
worksheet.write("D1", "Prices")



for item in range(len(brands)):
    worksheet.write(item+1, 0, brands[item])
    worksheet.write(item+1, 1, models[item])
    worksheet.write(item+1, 2, ages[item])
    worksheet.write(item+1, 3, prices[item])

y = len(brands)
#average price
worksheet.write("E1","Formulas")
worksheet.write("E2","Average price:")
worksheet.write("E3","Average age:")
worksheet.write_formula("F2","=average(D2:D1000)")
worksheet.write_formula("F3","=average(C2:C1000)")

workbook.close()




