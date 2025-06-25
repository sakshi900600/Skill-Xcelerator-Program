#  Add patient:

all_patients = {}


def add_Patient():

    patient_id = input("Enter patient id: ").strip()

    if patient_id in all_patients:
        print(f"Error! Patient {patient_id} already exists.")
        return None

    patient = {
        "name" : input("Enter patient name: ").strip().capitalize(),
        "age" : int(input("Enter patient age: ")),
        "gender" : input("Enter patient gender: ").capitalize(),

        "vitals" : {
            "temperature" : float(input("Enter temperature: ")),
            "bp" : input("Enter bp of patient (ex-120/80): "),
            "hr" : int(input("Enter patient heart rate: "))
        }
    }

    all_patients[patient_id] = patient

    print(f"Patient {patient['name']} added successfully! 🎉")


def view_all_patients():

    return all_patients


def search_patient():
    id = input("Enter patient id: ").strip()

    return all_patients[id]


def update_patient():
    id = input("Enter patient id: ").strip()

    updated_patient = "djl"



def delete_patient():
    id = input("Enter id of patient to delete: ")
    deleted_pat = "dsfljk"





while True: 
    print("\n --------- Welcome to the health management system 😇 --------- \n")

    print("Choose an option to perform operation on records: ")
    print("option-1: to add patient ✅")
    print("option-2: to view all patient 👀")
    print("option-3: to search patient by id 🔍")
    print("option-4: to update patient vitals 🌡️")
    print("option-5: to delete patient ❌")

    option = input("Enter your option no: ").strip()

    if option == "1":
        add_Patient()
    elif option == "2":
        view_all_patients()
    elif option == "3":
        search_patient()
    elif option == "4":
        update_patient()
    elif option == "5":
        delete_patient()
    else:
        print("Invalid option ❌. Try again ")


