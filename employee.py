class Employee1:
     def AcceptEmp1(self):
          self.Id=int(input("Enter emp1 id:"))
          self.Name=input("Enter emp1 name:")
          self.Dept=input("Enter emp1 Dept:")
          self.Sal=int(input("Enter emp1 Salary:"))
     def DisplayEmp1(self):
          print("Emp1 id:",self.Id)
          print("Emp1 Name:",self.Name)
          print("Emp1 Dept:",self.Dept)
          print("Emp1 Salary:",self.Sal)
class Manager(Employee1):
     def AcceptMgr(self):
         self.bonus=int(input("Enter Manager Bonus"))
     def DisplayMgr(self):
          print("Manger Bonus is:",self.bonus)
          self.TotalSal=self.Sal+self.bonus
          print("Total Salary: ", self.TotalSal)
n=int(input("Enter How may Managers:"))
lst=[]
for i in range(0,n):
     obj=input("Enter Object Name:")
     lst.append(obj)
print(lst)
for j in range(0,n):
     lst[j]=Manager()
     lst[j].AcceptEmp1()
     lst[j].AcceptMgr()
     print("\nDisplay Details of Manager",j+1)
     lst[j].DisplayEmp1()
     lst[j].DisplayMgr()
maxTotalSal= lst[0].TotalSal
maxIndex=0
for j in range(1,n):
       if lst[j].TotalSal > maxTotalSal:
             maxTotalSal= lst[j].TotalSal
             maxIndex=j
print("\nDisplay Details of Manager Having Maximum Salary(Salary+Bonus)")
lst[maxIndex].DisplayEmp1()
lst[maxIndex].DisplayMgr()