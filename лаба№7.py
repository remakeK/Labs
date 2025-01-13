class Employee:
    
    def __init__(self,*args,**data):
        self.name=data.get("name","Unknown")
        self.ind=data.get("id",None)
        
    def get_info(self):
        print(f"Сотрудник: {self.name}, Id: {self.ind}")

class Manager(Employee):
    
    def __init__(self,*args,**data):
        super().__init__(self,**data)
        self.department=data.get("department","Unknown")
    
    def manage_project(self):
        print(f"Менеджер {self.name} управляет проектом в отделе {self.department}")

class Technician(Employee):
    
    def __init__(self,*args,**data):
        super().__init__(self,**data)
        self.specialization=data.get("specialization","general")
    
    def perform_maintenance(self):
        print(f"Техник {self.name} выполняет техническое обслуживание по своей специализации: {self.specialization}")
        
class TechManager(Manager,Technician):
    
    def __init__(self,*args,**data):
        super().__init__(self,**data)
        self.team=[]
    
    def add_employee(self,name):
        self.team.append(name)
    
    def get_team_info(self):
        return self.team

emp1 = Technician(name="Николай",id=1,specialization="Инженер")
emp2 = Manager(name="Олег",id=2,department="Связи")
emp3 = Employee(name="Никита",id=3)


tech_manager = TechManager(name="Сергей",id=0,department="Свзяи",specialization="Главный Инженер")
tech_manager.add_employee(emp1.name)
tech_manager.add_employee(emp2.name)
tech_manager.add_employee(emp3.name)

tech_manager.get_team_info()
tech_manager.manage_project()
tech_manager.perform_maintenance()
print(tech_manager.get_team_info())
