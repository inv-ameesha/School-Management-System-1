from student import register_student,get_students
from auth import login
def showMenu():
    print("1.Registration 2.Students list")

def main():
    if not login():
        return
    showMenu()
    choice=int(input("Enter a choice"))
    if choice==1:
        register_student()
    elif choice==2:
        get_students()
    else:
        print("Invalid")

if __name__ == "__main__":
    main()