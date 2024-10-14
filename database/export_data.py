import pandas as pd
from django.db.models import Count
from guest.models import Student 

def export_students_to_excel(file_path):
    # Query to get the necessary data
    students = Student.objects.annotate(visits=Count('my_visits')).values('registration', 'student_name', 'visits')
    
    # Convert to DataFrame
    df = pd.DataFrame(list(students))
    
    # Specify the file name and path
    output_file = file_path
    
    # Export DataFrame to Excel
    df.to_excel(output_file, index=False, engine='openpyxl')  # Use the openpyxl engine to handle .xlsx files

    print(f"Data exported successfully to {output_file}")

# Specify the file path for the Excel file
excel_file_path = r'C:\Users\sergio\Desktop\students_data.xlsx'  # Adjust the file path as necessary

# Call the function to export data
export_students_to_excel(excel_file_path)
