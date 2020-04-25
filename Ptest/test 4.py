class Car:

    def __init__(self,color='white', quant_tyres=4):
        self.color=color
        self._tyres = [0 for i in range(0,quant_tyres)]

    def setDiam(self, number, value):

        if number<=len(self._tyres):
            self._tyres[number-1]=value
    def __str__(self):
        return str(len(self._tyres))

    def __iter__(self):
        for i in self._tyres:
            yield i

car1=Car(color='black', quant_tyres=4)
car1.setDiam(1,7)
car1.setDiam(2,4)
car1.setDiam(3,5)
car1.setDiam(4,8)

car2=Car(quant_tyres=2)
car2.setDiam(1,4)
car2.setDiam(2,1)
# for i in Car:
#     print(i.tyre)
# print(car1,car2)
for i in car1:
     print(car1, i)

for i in car2:
     print(car2, i)
