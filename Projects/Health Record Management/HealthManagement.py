#  Add patient:

all_patients = {}


def add_Patient():

    patient_id = input("Enter patient id: ").strip()

    if patient_id in all_patients:
        print(f"Error! Patient {patient_id} already exists.")
        return None

    name = input("Enter patient name: ").strip().capitalize()
    age = int(input("Enter patient age: "))
    gender = input("Enter gender: ").strip()

    print("\n Add vitals detials: ")

    temp = float(input("Enter temperature: "))
    bp = input("Enter bp (ex-120/80): ").strip()
    hr = int(input("Enter heart rate: "))

    all_patients[patient_id] = {
        "name" : name,
        "age" : age,
        "gender" : gender,
        "vitals": {
            "temp": temp,
            "bp": bp,
            "hr": hr
        }
    }

    print(f"\n✅ Patient '{name}' added successfully!")


def view_all_patients():
    print("\n🧑 Patient Records: ")
    
    print("--------------------------------------------------------- ")

    if not all_patients:
        print('No patient record found.')
        return 


    for patient_id , pt_data in all_patients.items():
        print(f"ID: {patient_id} | Name: {pt_data["name"]} | Age: {pt_data["age"]} | Temp: {pt_data["vitals"]['temp']}°F | BP: {pt_data["vitals"]["bp"]} | HR: {pt_data["vitals"]["hr"]} bpm ")

        print("---------------------------------------------------------- ")



def search_patient():
    print("\n🔍 Search Patient")
    id = input("Enter patient id: ").strip()

    isfound = False

    for pt_id , pt_data in all_patients.items():

        if pt_id == id:
            isfound = True

            print("\n🧾 Patient record found.")
            print("------------------------------------------")
            print(f"ID: {pt_id} | Name: {pt_data["name"]} | Age: {pt_data["age"]} | Temp: {pt_data["vitals"]['temp']}°F | BP: {pt_data["vitals"]["bp"]} | HR: {pt_data["vitals"]["hr"]} bpm ")
            print("------------------------------------------")
            health_alert(pt_id)


    if not isfound:
        print("\n❌ No matching patient found.")



def update_patient():
    print("\n Update Patient Vitals")
    id = input("Enter patient id: ").strip()

    for pt_id, pt_data in all_patients.items():
        if pt_id != id:
            print(f"Patient with {id} not found.")
            return 
        

        vitals = pt_data["vitals"]

        print("\n Enter new vitals: ")
        temp = float(input("Enter temperature: "))
        bp = input("Enter bp (e.g:120/80): ")
        hr = input("Enter heart rate: ")

        vitals["temp"] = temp
        vitals["bp"] = bp
        vitals["hr"] = hr

        print("Patient vitals updated successfully.")
        health_alert(pt_id)



def delete_patient():
    print("\n🗑 Delete Patient Record")
    id = input("Enter id of patient to delete: ").strip()

    if id in all_patients:
        name = all_patients[id]['name']
        del all_patients[id]
        print(f"\n🗑 Patient record for ID '{id}' ({name}) deleted.")
    else:
        print(f"❌ Patient with ID '{id}' not found!")

    

def health_alert(patient_id):
    patient = all_patients[patient_id]
    vitals = patient["vitals"]

    temp = vitals["temp"]
    bp = vitals["bp"]
    hr = vitals["hr"]

    if temp > 100:
        print("\n⚠️  Temperature is in critical range.")
    
    if int(hr) > 100:
        print("\n⚠️  Heart rate is in critical range")

    bp = bp.split("/")

    if int(bp[0]) > 140 or int(bp[1]) >90:
        print("\n⚠️  Blood pressure is in critical range.")





def main():
    while True: 
        print("\n --------- Welcome to the health management system 🩺 --------- \n")

        print("Choose an option to perform operation on records: ")
        print("1: to add patient ✅")
        print("2: to view all patient 👀")
        print("3: to search patient by id 🔍")
        print("4: to update patient vitals 🌡️")
        print("5: to delete patient ❌")
        print("6: to exit")

        option = input("\nEnter your option no: ").strip()

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
        elif option == "6":
            print("\nThank you for visiting 🤝")
            break
        else:
            print("Invalid option ❌. Try again ")
        
        input("\n Press Enter to continue...")


main()