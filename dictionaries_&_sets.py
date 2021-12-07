####################################################################################################################################################################
country_codes = {'Finland': 'fi', 'South Africa': 'za', 'Nepal': 'np'}

# checking if dict is empty
if country_codes:
    print('country_codes is not empty')
else:
    print('country_codes is empty')

####################################################################################################################################################################
details = {'Firstname': 'fname', "Lastname": 'lname'}

####################################################################################################################################################################
# Iterating through a Dictionary 
"""The following dictionary maps month-name strings to int values representing the numbers of days in the corresponding month. Note that multiple keys can have the 
same value:"""

days_per_month = {'January': 31, 'February': 28, 'March': 31}

for month, days in days_per_month.items():
    print(f'{month} has {days} days')

####################################################################################################################################################################
months = {'January': 1, 'February': 2, 'March': 3}

for month_name in months.keys():
    print(month_name, end=' ')

for month_number in months.values():
    print(month_number, end=' ')

####################################################################################################################################################################
names = {'Amo': 1, 'Lilly': 2, 'Deiv': 3, 'Nolly': 4}
for name_key in names.keys():
    print(name_num)

for name_value in names.values():
    print(name_value)
####################################################################################################################################################################
# Mini-Project
# Dictionary of Student Grades

"""The following script represents an instructor’s grade book as a dictionary that maps each
student’s name (a string) to a list of integers containing that student’s grades on three
exams. In each iteration of the loop that displays the data, we unpack a key–
value pair into the variables name and grades containing one student’s name and the corresponding list of three grades."""
# fig06_01.py
"""Using a dictionary to represent an instructor's grade book."""
grade_book = {