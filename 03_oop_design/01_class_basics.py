class Developer:
    def __init__(self , name, stack):
        self.name = name
        self.stack = stack

    def show_profile(self):
        print(f"Developer:{self.name}")
        print(f"Tech Stack: {','.join(self.stack)}")  

ankur = Developer('Ankur',["MongoDB", "Express", "React", "Node.js"])
ankur.show_profile()          