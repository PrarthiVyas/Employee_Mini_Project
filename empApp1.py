
emp_final=[]
flag=False
emp_name=""
def addemp():
    
    print("Add employee")
    emp=[]
    id2=input("ID: ")
    name=input("Name: ")
    designation=input("Designation: ")
    salary=int(input("Salary: "))
    status=input("Status: ")
    
    emp.append(id2)
    emp.append(name)
    emp.append(designation)
    emp.append(salary)
    emp.append(status)
    emp_final.append(emp)
    


def findemp():
    print("Find Employee Details")
    name=input("Enter a employee name which you want to find: ")
    for i in range(len(emp_final)):

        if name==emp_final[i][1]:
            print("\nID: ",emp_final[i][0])
            print("Name: ",emp_final[i][1])
            print("Designation: ",emp_final[i][2])
            print("Salary: ",emp_final[i][3])
            print("Status: ",emp_final[i][4])
            break
            
    else:
            
        print("\nSorry,This contact is not in the list")
    
            
            
def listemp():
    
    
    for i in range(len(emp_final)):
        if emp_final[i][4]=="active" or emp_final[i][4]=="Active":
            print("\nnList all employees")
            print("\nID: ",emp_final[i][0])
            print("Name: ",emp_final[i][1])
            print("Designation: ",emp_final[i][2])
            print("Salary: ",emp_final[i][3])
            print("Status: ",emp_final[i][4])
            print("----------------------")
            break
        else:
            print("List is empty")

        
def incre_decre():
    print("Find Employee Details")
    name=input("Enter a employee name which you want to find: ")
    for i in range(len(emp_final)):

        if name==emp_final[i][1]:
            choice=int(input("Select 1 or 2 for Increment or Decrement: "))
            if choice==1:
                global emp_name
                global flag
                print("\nCongratulations!!you get increment of 30%")
                
                print("\nID: ",emp_final[i][0])
                print("Name: ",emp_final[i][1])
                print("Designation: ",emp_final[i][2])
                
        
                count=((emp_final[i][3]*30)/100)+emp_final[i][3]
                emp_final[i][3]=count
                print("Salary: ",emp_final[i][3])
                print("Status: ",emp_final[i][4])
                
                emp_name=emp_final[i][1]
               
                flag=True
                break
            
            elif choice==2:
                
                print("\nsorry!!you get decrement of 30% because of your poor work")
                print("\nID: ",emp_final[i][0])
                print("Name: ",emp_final[i][1])
                print("Designation: ",emp_final[i][2])
                count=emp_final[i][3]-((emp_final[i][3]*30)/100)
                emp_final[i][3]=count
                print("Salary: ",emp_final[i][3])
                print("Status: ",emp_final[i][4])
                emp_name=emp_final[i][1]
                break
                       
            else:
                print("\nInvalid choice")
                break
               
    else:
            
        print("\nSorry,This contact is not in the list")
def delemp():
    name=input("Enter a name which you want to delete: ")
    
    for i in range(len(emp_final)):
        if emp_final[i][1]==name:
            print("This data is removed")
            del emp_final[i]
            break
    else:
        print("This contact is not in the list")
    
        
def promodemo():
    name=input("Enter a name for which you want to find promotion or demotion: ")
    for i in range(len(emp_final)):
        if emp_final[i][4]=="active" or emp_final[i][4]=="Active":
            if flag==True and name==emp_name:
                print("\nCongratulations!",emp_name,"got promotion")
                break
            elif flag==False and name==emp_name:
                print("\nSorry",emp_name,"got demotion")
                break
        else:
             print("He is not working in the company right now")
             break
    else:
        print("\nThis contact is not in the list")
                
            

while True:
    print("\n\t Employee Details")
    print("1. Add employee")
    print("2. Find employee")
    print("3. List employee")
    print("4. Increment/Decrement")
    print("5. Promotion/Demotion")
    print("6. Delete employee")
    print("7. QUIT")
    print("----------------------")


    choice=int(input("Enter a choice no: "))

    if choice==1:
        addemp()

    if choice==2:
        findemp()
    if choice==3:
        listemp()
    if choice==4:
        incre_decre()
    if choice==5:
        promodemo()
    if choice==6:
        delemp()
    if choice==7:
        break
