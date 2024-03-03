import datetime

complaints_list = []

def register_complaint(title, description):
    complaint_id = len(complaints_list) + 1
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_complaint = {
        "id": complaint_id,
        "title": title,
        "description": description,
        "status": "Pending",
        "timestamp": timestamp,
    }

    complaints_list.append(new_complaint)
    return complaint_id

def view_all_complaints():
    return complaints_list

def view_complaint(complaint_id):
    for complaint in complaints_list:
        if complaint["id"] == complaint_id:
            return complaint
    return None

def update_complaint_status(complaint_id, status):
    for complaint in complaints_list:
        if complaint["id"] == complaint_id:
            complaint["status"] = status
            return True
    return False

def main():
    while True:
        print("\nComplaint Management System")
        print("1. Register a Complaint")
        print("2. View All Complaints")
        print("3. View a Complaint")
        print("4. Update Complaint Status")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter complaint title: ")
            description = input("Enter complaint description: ")
            complaint_id = register_complaint(title, description)
            print(f"Complaint registered successfully. Complaint ID: {complaint_id}")

        elif choice == "2":
            complaints = view_all_complaints()
            for complaint in complaints:
                print(complaint)

        elif choice == "3":
            complaint_id = int(input("Enter complaint ID: "))
            complaint = view_complaint(complaint_id)
            if complaint:
                print(complaint)
            else:
                print("Complaint not found.")

        elif choice == "4":
            complaint_id = int(input("Enter complaint ID: "))
            status = input("Enter new status: ")
            if update_complaint_status(complaint_id, status):
                print("Complaint status updated successfully.")
            else:
                print("Complaint not found.")

        elif choice == "5":
            print("Exiting the Complaint Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
