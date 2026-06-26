class Developer:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary   # __ is used to make the variabel private

    def show_salary(self):
        print(f"{self.name} : {self.__salary}")    

    def update_salary(self,amount):
        if amount > 0 :
           self.__salary = amount
           print('salary is updated Successfully!')

# creating Object
ankur = Developer("Ankur",100000)
ankur.show_salary()


# Updating the Salary
ankur.update_salary(200000)
ankur.show_salary()






























