import csv
from datetime import date

def mark_attendance():
 
    student_id = input("Enter Student ID: ").strip()
    status = input("Enter status (P/A): ").strip().upper()

    
    if status not in ['P', 'A']:
        print("Invalid status. Please enter 'P' or 'A'.")
        return

    today = date.today().strftime("%Y-%m-%d")
    
    
    with open('attendance_logs.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([today, student_id, status])
    print(f"Attendance recorded for Student ID: {student_id}")



print("Hello User! Welcome to the Attendance System.")
print("To start, press 'R'. To exit at any time, press 'Q'.")

while True:
    choice = input("Enter your choice (R/Q): ").strip().upper()
    
    if choice == 'R':
        mark_attendance()
        print("\nReady for next entry.")
    elif choice == 'Q':
        print("Exiting the attendance system. Goodbye!")
        break  
    else:
        print("Invalid choice. Please enter 'R' to record attendance or 'Q' to quit.")