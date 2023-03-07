class car :
    #class attributes
    def __init__ (self,model,make,year_of_manufacture,engine_capacity):
        #instance attributes
        self.model = model
        self.make = make 
        self.year_of_manufacture = year_of_manufacture
        self.engine_capacity = engine_capacity

#getters->used to get the values
    def get_model(self):
        return self.model
    def get_make(self):
        return self.make
    def get_year_of_manufacture(self):
        return self.year_of_manufacture
    def get_engine_capacity(self):
        return self.engine_capacity
    
#setters-->set the attributes
    def set_model(self,model):
        self.model = model
    def set_make(self,make):
        self.make = make
    def set_year_of_manufacture(self,model):
        self.year_of_manufacture = year_of_manufacture
    def set_engine_capacty(self,engine_capacity):
        self.engine_capacity = engine_capacity

    
car1 = car("demio","mazoa",2018,1300)
car2 = car("hilux","nissan",2022,3000)
car3 = car("teana","nissan",2020,2500)




print(car1.get_model())
print(car1.get_year_of_manufacture())

print(car2.get_model())
print(car2.get_year_of_manufacture())

print(car3.get_model())
print(car3.get_year_of_manufacture())

