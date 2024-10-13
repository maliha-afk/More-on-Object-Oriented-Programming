class Tesla:
    def __init__(self,Name,ID,Salary):
        self.Name=Name
        self.ID=ID
        self.Salary=Salary

    def getdetails(self):
        print(f"Name: {self.Name}, ID: {self.ID}, Salary: {self.Salary}")

emp1=Tesla("Atiya",2345,900000)
emp2=Tesla("Adib",3125,750000)

emp1.getdetails()
emp2.getdetails()
