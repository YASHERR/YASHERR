"CMS"
"""Operatios: Add Customer, Search Customer, Delete Customer, Modify Customer,
Display All Customers, Exit
Particular Customer: id,name,age,mob
Object is the real time entity and class is a blueprint of object 
"""
#BLL
class Customer:
    cuslist=[]      #[1000,2000,3000]
    def __init__(self):
        self.id=0
        self.name=0
        self.age=0
        self.mob=0
    def addCustomer(self):
        Customer.cuslist.append(self)
    def searchCustomer(self):   #self=8000,self.id=20, self.name=0, self.age=0, self.mob=0
        for e in Customer.cuslist:
            if(e.id==self.id):      #Firste=1000, Seconde=2000
                self.name=e.name         #8000.name=self.name="Anil"
                self.age=e.age
                self.mob=e.mob
                return
    @staticmethod
    def deleteCustomer(id):     #id=20
        for e in Customer.cuslist:
            if(e.id==id):
                Customer.cuslist.remove(e)
                return
    def modifyCustomer(self):   #self=12000, self.id=30, self.name="Sonu", self.age=22, self.mob=5555
        for e in Customer.cuslist:
            if(e.id==self.id):
                e.name=self.name
                e.age=self.age
                e.mob=self.mob
                return 1
        return 0

#PL
print("Welcome to Prashant's CMS")
def showCustomer(cus):      #cus=8000
    print("Cust ID:",cus.id,"Cust Name:",cus.name,"Cust Age:",cus.age,"Cust Mob:",cus.mob )
while(1):
    print("Enter 1 for Add Cust, 2 for Search Cust")
    print("3 for Delete Cust, 4 for Modify Cust")
    print("5 for Display All Cust, 6 for Exit")
    choice=input("Enter Choice 1 to 6:")
    if(choice=="1"):    #Add Customer
        cus=Customer()  #cus=1000, cus.id=0, cus.name=0, cus.age=0, cus.mob=0
        cus.id=input("Enter Cust Id:")      #10
        cus.name = input("Enter Cust Name:")    #"Vikas"
        cus.age = input("Enter Cust Age:")      #39
        cus.mob = input("Enter Cust Mob:")      #"1234"
        cus.addCustomer()   #formal=actual, self=cus
        print("Customer Added Successfully")
    elif(choice=="2"):  #Search Customer
        cus=Customer()  #cus=8000, cus.id=0, cus.name=0, cus.age=0, cus.mob=0
        cus.id=input("Enter Cust Id:")  #cus.id=20, cus.name=0, cus.age=0, cus.mob=0
        cus.searchCustomer()    #cus.name=8000.name="Anil", cus.age=41, cus.mob=2345
        showCustomer(cus)
    elif(choice=="3"): #Delete Customer: Static Method
        id=input("Enter Cust Id:")  #id=20
        Customer.deleteCustomer(id)
        print("Customer Deleted Successfully")
    elif(choice=="5"):  #Display All Customer:
        for e in Customer.cuslist:
            showCustomer(e)
    elif (choice == "4"):  # Modify Customer
        cus = Customer()  # cus=12000, cus.id=0, cus.name=0, cus.age=0, cus.mob=0
        cus.id = input("Enter Cust Id:")  # 30
        cus.name = input("Enter Cust Updated Name:")  # "Sonu"
        cus.age = input("Enter Cust Updated Age:")  # 22
        cus.mob = input("Enter Cust Updated Mob:")  # "5555"
        flag=cus.modifyCustomer()  # formal=actual, self=cus
        if(flag==1):
            print("Customer Modified Successfully")
        else:
            print("Customer Id not Found")
    elif (choice == "6"):  # Exit
        print("Thanks for using Prashant's CMS")
        break

