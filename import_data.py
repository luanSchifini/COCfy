import pandas as pd
from guest.models import Eletiva, Group, Guest, Student


def import_data_from_excel(excel_file_path):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(excel_file_path)

    # Loop through each row in the DataFrame and save the data to your database
    for index, row in df.iterrows():
        # Extract data from the Excel file columns (adjust column names as needed)
        eletiva_name = row['eletiva']
        group_name = row['Group Name']
        #guest_name = row['Guest Name']
        #email = row['Email']
        #verification_code = row['Verification Code']
        student_name = row['aluno']

        # Create or get Eletiva and Group instances
        eletiva, created = Eletiva.objects.get_or_create(eletiva_name=eletiva_name)
        group, created = Group.objects.get_or_create(group_name=group_name, eletiva=eletiva)

        # Create Guest instance
        #guest, created = Guest.objects.get_or_create(name=guest_name, email=email)
        #guest.verification_code = verification_code
        #guest.save()

        # Create or get Student instance
        student, created = Student.objects.get_or_create(student_name=student_name, eletiva_group=group)

    print("Data import from Excel completed.")


excel_file_path = 'securecoc-main/securecoc/TURMAS_2023_2_1.xlsx'


import_data_from_excel(excel_file_path)