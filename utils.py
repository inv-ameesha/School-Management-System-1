import re
def validate_name(name):
    return len(name)>=2 and name.replace(" ","").isalpha

def validate_age(age):
    return age.isdigit() and 18<=int(age)<=25

def validate_email(email):
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_pattern, email) is not None

def  validate_phone(phone):
    pattern = r"^\d{10}$"
    return re.match(pattern, phone) is not None

course_list = ["BCA", "BTECH", "BCOM", "BSC", "BA"]

def get_course():
    print("Available courses are:")
    for i, course in enumerate(course_list):
        print(f"{i+1}: {course}")

    choice = input("Enter a choice: ")
    if choice.isdigit() and 1 <= int(choice) <= len(course_list):
        return course_list[int(choice) - 1]
    else:
        print("Invalid course choice.")
        return None



    

