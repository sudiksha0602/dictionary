student_details = {'name':'kirti','age':18,'location':'bengal','country':'indian'}
new_dict = {key:student_details[key]for key in student_details.keys()-['name','age']}
print(new_dict)