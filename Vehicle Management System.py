#Python Project on Vehicle Data

import pickle
import os
import sys

#************************************************************************
def create_record():
    print("\n")
    f=open("Vehicles.dat", 'wb')
    while True:
        L=[]
        veh_no = input("\nEnter the Vehicle Number: ")
        L.append(veh_no)
        veh_company = input("\nEnter the Vehicle's Company: ")
        L.append(veh_company)
        veh_wheels = int(input("\nEnter the No. of wheels: "))
        L.append(veh_wheels)
        pickle.dump(L, f)
        ch=input("Do you want to enter more records?(Y/N) ")
        if ch in 'yY':
            continue
        else:
            break
    f.close()



#************************************************************************
def print_whole():
    print("\n")
    f=open("Vehicles.dat", "rb")
    try:
        while True:
            R=pickle.load(f)
            print(R)
    except EOFError:
        f.close()    

#************************************************************************
def record_entry():
    print("\n")
    print("Enter Vehicle Details: ")
    print("\n")
    f=open("Vehicles.dat", 'ab')
    while True:
        L=[]
        veh_no = input("\nEnter the Vehicle Number: ")
        L.append(veh_no)
        veh_company = input("\nEnter the Vehicle's Company: ")
        L.append(veh_company)
        veh_wheels = int(input("\nEnter the No. of wheels: "))
        L.append(veh_wheels)
        pickle.dump(L, f)
        ch=input("Do you want to enter more records?(Y/N) ")
        if ch in 'yY':
            continue
        else:
            break
    f.close()


#************************************************************************
def record_search():
    print("\n")
    try:
        f=open("Vehicles.dat", 'rb')
    except FileNotFoundError:
        print("File not found")
        return
    sr=int(input("Enter Vehicle number to search: "))
    try:
        while True:
            R=pickle.load(f)
            if R[0]==A:
                print("Record found")
                print(R)
                break
    except EOFError:
        print("Record not found")
    f.close() 

#************************************************************************
def record_update():
    print("\n")
    try:
        f=open("Vehicles.dat", 'rb+')
    except FileNotFoundError:
        print("File not found")
        return
    A=int(input("Enter Vehicle number to be updated:"))
    pos=0
    try:
        while True:
            R=pickle.load(f)
            print("What would you like to change: ")
            tc=input("Press 1 for Company or 2 for no. of wheels: ")
            if tc==1:
                if R[0]==A:
                    f.seek(pos)
                    P=float(input("Enter the New Company: "))
                    R[2]=P
                    pickle.dump(R, f)
                    print("Record updated")
                    break
                else:
                    pos=f.tell()
            elif tc==2:
                if R[0]==A:
                    f.seek(pos)
                    P=float(input("Enter the New no. of wheels: "))
                    R[2]=P
                    pickle.dump(R, f)
                    print("Record updated")
                    break
                else:
                    pos=f.tell()
            else:
                print("Wrong Input\n")
    except EOFError:
        print("Record not found")
    f.close()    

#************************************************************************
def record_delete():
    print("\n")
    try:
        f1=open("Vehicles.dat", 'rb')
    except FileNotFoundError:
        print("File not found")
        return
    f2=open("temp_new.dat", 'wb')
    A=int(input("Enter admission number to delete: "))
    found=0
    try:
        while True:
            R=pickle.load(f1)
            if R[0]==A:
                found=1
                continue
            pickle.dump(R,f2)
    except EOFError:
        f1.close()
        f2.close()
    os.remove("Vehicles.dat")
    os.rename("temp_new.dat", "Vehicles.dat")
    if found==1:
        print("Record deleted")
    else:
        print("Record not found")

#************************************************************************
def record_end():
    print("\n")
    sys.exit("\nEnd of PROJECT\nThank you\n         Credits:\n         Vedang")

#************************************************************************
while True:    
    print("\n\n")
    print("\t\tMAIN MENU")
    print("*********************************************")
    print("1. Create Record")
    print("2. Display Record")
    print("3. Append Record")
    print("4. Search Record")
    print("5. Update Record")
    print("6. Delete Record")
    print("7. Exit from Project")
    print("*********************************************")

    choice=int(input("Enter your choice between 1 to 7---->"))

    if choice==1:
        create_record()
    elif choice==2:
        print_whole()
    elif choice==3:
        record_entry()
    elif choice==4:
        record_search()
    elif choice==5:
        record_update()
    elif choice==6:
        record_delete()
    elif choice==7:
        record_end()
    else:
        print("\nWrong Choice!\n\nTry again")

#************************************************************************

#END OF PROJECT
