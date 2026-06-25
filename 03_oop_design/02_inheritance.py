class Developer:
    def __init__(self,name,stack):
        self.name=name
        self.stack=stack
  
    def show_profile(self):
        print(f"Developer: {self.name} , Stack: {','.join(self.stack)}")

# Inheritance: SeniorDeveloper, Developer
class SeniorDeveloper(Developer):
    def __init__(self, name, stack, experience_years):
        # super() is used to call the parent class init method
        super().__init__(name, stack)
        self.experience_years = experience_years

    def show_profile(self):
        # overiding the parent method
        super().show_profile()
        print(f"Years of Experience: {self.experience_years}")

#  creating Object
ankur_senior = SeniorDeveloper("Ankur", ["MongoDB", "Express", "React", "Node.js"], 10)
ankur_senior.show_profile()     
            
 
