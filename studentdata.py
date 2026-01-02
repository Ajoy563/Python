studata={}
while(1):
    print("\n1. Add student Data\n2. Remove Data\n3. Display Data\n4. Exit")
    c=int(input("\nEnter your choice: "))
    if c==1:
        name=input("Enter student name: ").upper()
        if name in studata:
            print("\nStudent already exists!")
        else :
            Class=input("Enter class: ").upper()
            sub=input("Enter the subjects with space: ").upper()
            studic= {"Name":name,"Class":Class,"Subjects":sub}
            studata[name]=studic
        print("\nStudent data added successfully!")
    elif c==2:
        remove=input("To remove the student data, Enter the student name: ").upper()
        studata.pop(remove,None)
        print("\nStudent Data removed successfully!")

    elif c==3:
        print("\nName\tClass\tSubjects\n")
        for name, data in studata.items():
            print(f"{data['Name']}\t{data['Class']}\t{data['Subjects']}")
    elif c==4:
        break
    else:
        print("\nInvalid Choice!")