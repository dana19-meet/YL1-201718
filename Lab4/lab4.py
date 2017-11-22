##class Animal(object):
##    def __init__(self,sound,name,age,fcolor):
##        self.sound=sound
##        self.name=name
##        self.age=age
##        self.fcolor=fcolor
##    def eat(self,food):
##        print("yummy!! "+self.name+" is eating "+food)
##    def description(self):
##        print(self.name+" is "+str(self.age)+" years old and loves the color "+self.fcolor)
##    def ms(self,num):
##        print(num*self.sound)
##cat=Animal("meow","tom",2,"pink")
##cat.eat("fish")
##cat.description()
##cat.ms(5)

##class Person(object):
##    def __init__(self,name,age,city,gender,haircolor):
##        self.name=name
##        self.age=age
##        self.city=city
##        self.gender=gender
##        self.haircolor=haircolor
##    def eat(self,favfood):
##        print("yummm! im eating "+favfood)
##
##dana=Person("dana",15,"tivon","female","brown")
##dana.eat("pasta")

class song(object):
    def __init__(self,lyrics):
        self.lyrics=lyrics
    def sing(self):
        for i in self.lyrics:
            print(i)

flowersong=song(["roses are red,",
       "violets are blue,",
       "i wrote this poem for you."])
flowersong.sing()































