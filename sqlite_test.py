import sqlite3
def addstudent():
    a=sqlite3.connect("students.db")
    c=a.cursor()
    while True:
        Name=input("Enter Name:")
        if(Name.strip()==""):
            print("Name Cannot Be Empty")
        elif not all(char.isalpha() or char.isspace() for char in Name):
            print("Name Can Only Contain Letters And Spaces")
        else:
            break
            
    while True:
        try:
            Age=int(input("Enter Age:"))
            if(Age<=0):
                print("Enter Valid Age")
            else:
                break
        except ValueError:
            print("Enter Numbers Only")
            
    while True:
        print("1 - CSE\n2 - ELE\n3 - MEC\n4 - AA\n5 - CIVIL")
        try:
            Course=int(input("Enter Your Course Number:"))
            if(Course==1):
                Course="CSE"
                break
            elif(Course==2):
                Course="ELE"
                break
            elif(Course==3):
                Course="MEC"
                break
            elif(Course==4):
                Course="AA"
                break
            elif(Course==5):
                Course="CIVIL"
                break
            else:
                print("Enter Valid Course Number")
        except ValueError:
            print("Enter Numbers Only")
                
    c.execute("""INSERT INTO students (Name,Age,Course)
              VALUES(?,?,?)""",(Name.title(),Age,Course))
    a.commit()
    c.close()
    a.close()
    print("Student Added Successfully\n")
    
def viewstudent():
    a=sqlite3.connect("students.db")
    c=a.cursor()
    c.execute("""SELECT * FROM students""")
    data=c.fetchall()
    if not data:
        print("No Records")
    else:
        cln=c.description
        for j in data:
            print(f"{cln[0][0]}: {j[0]}")
            print(f"{cln[1][0]}: {j[1]}")
            print(f"{cln[2][0]}: {j[2]}")
            print(f"{cln[3][0]}: {j[3]}\n")
            
    c.close()
    a.close()

def searchstudent():
    a=sqlite3.connect("students.db")
    c=a.cursor()
    while True:
        try:
            id=int(input("Enter ID:"))
            if(id<=0):
                print("Enter Valid ID\n")
            else:
                break
        except ValueError:
            print("Enter Number Only\n")
            
    c.execute("""SELECT * FROM students WHERE ID = ?""",(id,))
    data=c.fetchone()
    if data is None:
        print("No Student Founded")
    else:
        cln=c.description
        for i in range(0,4):
            print(f"{cln[i][0]}: {data[i]}")
    c.close()
    a.close()
    
def updatestudent():
    a=sqlite3.connect("students.db")
    c=a.cursor()
    while True:
        try:
            id=int(input("Enter ID:"))
            if(id<=0):
                print("Enter Valid ID\n")
            else:
                break
        except ValueError:
            print("Enter Number Only\n")
    
    c.execute("""SELECT * FROM students WHERE ID =?""",(id,))
    data=c.fetchone()
    Courses= {1:"CSE",2:"ELE",3:"MEC",4:"AA",5:"CIVIL"}
    if data is None:
        print("No Student Founded")
    else:
        prevcourse=data[3]
        while True:
                try:
                    for i,j in Courses.items():
                        print(f"{i}: {j}")
                        
                    Course=int(input("Enter Your New Course Number:"))
                    
                    if(Course not in Courses):
                        print("Enter Valid Course Number")
                    elif(prevcourse==Courses[Course]):
                        print("Course Cannot Be Same As Previous")
                    else:
                        Course=Courses[Course]
                        break
                except ValueError:
                    print("Enter Numbers Only")
        
        c.execute("""UPDATE students SET Course =? WHERE ID =?""",
                  (Course,id))
        print("Record Updated!\n")
        a.commit()
        print("Updated Record:")
        c.execute("""SELECT * FROM students WHERE ID =?""",(id,))
        data=c.fetchone()
        cln=c.description
        for i in range(0,4):
            print(f"{cln[i][0]}: {data[i]}")
    c.close()
    a.close()

def deletestudent():
    a=sqlite3.connect("students.db")
    c=a.cursor()
    while True:
        try:
            id=int(input("Enter Id:"))
            if(id<=0):
                print("Enter Valid ID")
            else:
                break
        except ValueError:
            print("Enter Numbers Only")
    c.execute("SELECT * FROM students WHERE ID =?",(id,))
    data=c.fetchone()
    if data is None:
        print("No Record To Delete")
    else:
        print(f"Are You Sure To Delete ID:{id} Record")
        while True:
            try:
                confirmation=input("Enter Yes/No:")
                if(confirmation.lower()=="yes"):
                    c.execute("""DELETE FROM students WHERE ID =?""",(id,))
                    a.commit()
                    print("\nRecord Deleted!\n")
                    print("Updated Record")
                    c.execute("""SELECT * FROM students""")
                    data=c.fetchall()
                    if not data:
                        print("Data Is Empty")
                    cln=c.description
                    for i in data:
                        for j in range(4):
                            print(f"{cln[j][0]}: {i[j]}")
                        print()    
                    break

                elif(confirmation.lower()=="no"):
                    break
                
                else:
                    print("Enter Properly")
            except ValueError:
                print("Enter Numbers Only")
    c.close()
    a.close()
    
    

    
while True:
    print("\n__-----Student Management System-----__\n")
    print("1 - Add Student\n2 - View Record\n3 - Search Student\n4 - Update Student Record\n5 - Delete Student\n6 - Exit")

    try:
        choice = int(input("\nEnter Your Choice:"))

        if choice == 1:
            addstudent()

        elif choice == 2:
            viewstudent()

        elif choice == 3:
            searchstudent()

        elif choice == 4:
            updatestudent()

        elif choice == 5:
            deletestudent()

        elif choice == 6:
            break

        else:
            print("Invalid Choice")

    except ValueError:
        print("Enter Number Only")



