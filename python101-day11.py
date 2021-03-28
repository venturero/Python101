import xlsxwriter

cars =[]
brands = []
models = []
colors = []
ages = []
prices = []

x = int(input("How many cars do you have(int)?"))

while(x>0):
    brand = str(input("Brand(str):"))
    brands.append(brand)
    model = str(input("Model(str):"))
    models.append(model)
    color = str(input("Color(str):"))
    colors.append(color)
    age = int(input("Age(int):"))
    ages.append(age)
    price = int(input("Price(int):"))
    prices.append(price)
    print("*********************")
    x -= 1
print(brands)
print(models)
print(colors)
print(ages)
print(prices)

#cars.append(brands,models,colors,ages,prices)


workbook = xlsxwriter.Workbook("cars4.xlsx")
worksheet = workbook.add_worksheet("cars_list")

succes = workbook.add_format(
    {
        "bg_color":"#FFFF00",
        "font":"Calibri",
        "font_size":11,
        "bold":True
    }
)


cell_format = workbook.add_format({'bold': True, 'font_color': 'black'})#to change the letters color
cell_format.set_font_color("black")

row = 0
col = 0

yellow_fmt = workbook.add_format()
yellow_fmt.set_pattern(1)
yellow_fmt.set_bg_color('#FFFF00')

worksheet.write("A1","Brands",succes)
#worksheet.write("A1", "Brands",cell_format)#cell_format
worksheet.write("B1", "Models", succes)
worksheet.write("C1", "Ages", succes)
worksheet.write("D1", "Prices", succes)




for item in range(len(brands)):
    worksheet.write(item+1, 0, brands[item])
    worksheet.write(item+1, 1, models[item])
    worksheet.write(item+1, 2, ages[item])
    worksheet.write(item+1, 3, prices[item])

y = len(brands)
succes2 = workbook.add_format(
    {
        "bg_color":"#FF0000",
        "font":"Calibri",
        "font_size":11,
        "bold":True
    }
)
#average price
worksheet.write("E1","Formulas",succes2)
worksheet.write("E2","Average price:",succes2)
worksheet.write("E3","Average age:",succes2)
worksheet.write_formula("F2","=average(D2:D1000)")
worksheet.write_formula("F3","=average(C2:C1000)")

workbook.close()