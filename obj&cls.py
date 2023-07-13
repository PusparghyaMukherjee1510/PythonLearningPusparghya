# class Person():
#     def __init__(self) -> None:
#          self.name="Sam"
#          self.age=12
#          self.gender="Male"
#     def talk(self):
#          print("Hi, I\'m",self.name)
#     def vote(self):
#          if self.age<18:
#               print("I\'m unable to  Vote")
#          else :
#               print("I\'m able to Vote")

# obg=Person()
#Person.talk(obg)
#Person.vote(obg)
#different way to call class methods
# obg.talk()
# obg.vote()


#create multiple objects
# class Person():
#     def __init__(self,n,g,a) -> None:
#          self.name=n
#          self.age=a
#          self.gender=g
#     def talk(self):
#          print("Hi, I\'m",self.name)
#     def vote(self):
#          if self.age<18:
#               print("I\'m unable to  Vote")
#          else :
#               print("I\'m able to Vote")

# ojn=Person("DOP","Male",98)
# ojm=Person("Jass","Female",96)
# ojn.talk()
# ojn.vote()
# ojm.talk()
# ojm.vote()

# class Car():
#     def getSpeed(self,n,s):
#         self.name=n
#         self.speed=s
#         print("Name is ",self.name)
#         print("Speed is ",self.speed)

# ofd=Car()
# ofg=Car()
# ofd.getSpeed("BMW",120)
# ofg.getSpeed("TATA",80)
# Toy=Car()
# Car.getSpeed(Toy,"Toyota",78)

#Inheritance
class Car():
    def __init__(self,y,s):
        self.year=y
        self.speed=s
    def getYear(self):
        print("year is : ",self.year)
    def getSpeed(self):
        print("max speed : ",self.speed)

class Sedan(Car):
    def accLert(self):
        print(self.getSpeed())

class SUV(Car):
    def accLert(self):
        print(self.getSpeed())

BMW=Car(2013,155)
TATA=Sedan(2012,132)
Toyota=SUV(2006,110)

BMW.getSpeed()
BMW.getYear()
TATA.getSpeed()
TATA.getYear()
Toyota.getSpeed()
Toyota.getYear()

#Encapsulation
#Polymorphism
onbl=[Sedan("Camara",120),SUV("Mahindra",123)]
for i in onbl:
    print(i.year+ ":",end=" ")
    i.accLert()