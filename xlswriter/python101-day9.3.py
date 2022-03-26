
import xlsxwriter

class cars():
    def __init__(self,brand,model,color,price):
        self.brand  = brand
        self.model  = model
        self.color   = color
        self.price  = price
    def showinfos(self):
        print("Car info:")
        print("Brand: {}\nModel: {}\nColor: {}\nPrice: {}\n".format(self.brand,self.model,self.color,self.price))
    def zam_yap(self,zam_miktarı):
        self.maaş += zam_miktarı
    def __str__(self):
        return "Brand: {}\nModel: {}\nColor: {}\nPrice: {}".format(self.brand,self.model,self.color,self.price)
car1 = cars("Tesla","ModelS","red",73000)
car2 = cars("Opel","Astra","grey",35000)
car3 = cars("Porche","Taycan","blue",500000)
cars.__str__(self=car1)
car1.showinfos()
x = int(input("How many cars do you have?"))


while(x>0):
    brand = str(input("Brand:"))
    car1.brand
    model = str(input("Model:"))
    car1.model
    color = str(input("Color:"))
    car1.color
    price = int(input("Price:"))
    car1.price
    x-=1

cars.__str__(self=car1)
car1.showinfos()
