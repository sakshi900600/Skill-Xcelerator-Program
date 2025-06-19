name = input("Enter your name: ").strip(" ")
email = input("Enter your email: ").lower()
phone_no = input("Enter your phone no: ").strip()
experience = int(input("Enter your years of experience: "))
skills_input = input("Enter skills (comma-separated): ")

# strip() - when it is called without any argument it removes all the leading and trailing spaces. and if called with argument like any char it remove that char from start and end. 

skills = [
    skill.strip().capitalize()
    for skill in skills_input.split(",")
    if skill.strip()
]
formatted_skills = ", ".join(skills)


# print(f"Skills: {formatted_skills}")



formatted_name = name.split(" ")
for i in range(len(formatted_name)):
    word  = formatted_name[i]
    formatted_name[i] = word.capitalize()


name = " ".join(formatted_name)
# print(name)





def validate_email(email):
    if '@' in email and '.' in email.split('@')[-1] and " " not in email:
        return True
    return False


def validate_phone(phone):
    return (len(phone) == 10 and phone.isdigit())


def validate_experience(experience):
    if experience < 0:
        return False
    return True


def printResume(name,email,phone,experience,skills):
        print("\n\n ----------  Your Resume  -------------")
        print(f"Name: {name}")

        if validate_email(email):
            print(f"Email: {email}")
        else: 
            print("Invalid Email must contain @")

        if validate_phone(phone):
            print(f"Phone Number: {phone_no}")
        else:
            print("Phone must be of 10 digits")
        
        if validate_experience(experience):
            print(f"Years of Experience: {experience}")
        else:
            print("Please enter a non-negative integer")

        
        print(f"Skills: {skills}")



printResume(name,email,phone_no,experience, formatted_skills)





    
    
    
    
