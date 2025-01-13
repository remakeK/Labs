class UserAccount:
    
    def __init__(self,username,email,password):
        self.username=username
        self.email=email
        self.__password=password
        
    def set_password(self,new_password):
        self.__password=new_password
        
    def check_password(self,password):
        print(password==self.__password)
        
user=UserAccount("User1234","mail@gmail.com","1234")
user.set_password("4321")
user.check_password("4321")





class Vehicle:
    
    def __init__(self,make,model):
        self.make=make
        self.model=model
    
    def get_info(self):
        print(f"Марка: {self.make}, Модель: {self.model}")
    
class Car(Vehicle):
    
    def __init__(self,make,model,fuel_type):
        super().__init__(make,model)
        self.fuel_type=fuel_type
        
    def get_info(self):
        print(f"Марка: {self.make}, Модель: {self.model}, Тип топлива: {self.fuel_type}")
        
car=Car("Car","Model","бензин")
car.get_info()