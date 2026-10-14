class person:
    def __init__(self,name):
        self.name=name
    def display(self):
        return f"name : {self.name}"
class student(person):
    def __init__(self,name,rno):
        super().__init__(name)
        self.rno=rno
    def display(self):
        print(super().display())
        return f"rno : {self.rno}"
s=student("alisha",303)
print(s.display())
