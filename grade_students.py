percentages = [
    {'name':'Ali', 'Percentage':91},
    {'name':'Ben', 'Percentage': 89},
    {'name':'Alex', 'Percentage': 65},
    {'name':'Mitchael', 'Percentage':95},
    {'name': 'Starc', 'Percentage':50}
]

# if student got 95% or abpve A+ grade
# if got  90% or more but less then 95 give A grade
# for less the 90 but more than 80 give B
# for less then 80 but more then 70 give C
# for less then 70 but more then 60 give D
# else give F grade

grade = {}

for students in percentages:
    percentage = students['Percentage']
    name = students['name']
    if percentage >= 95:
        print("{} got A+ grade".format(name))
        grade[name] = 'A+'
    elif percentage > 90 and percentage < 95:
        print("{} got A grade".format(name))
        grade[name] = 'A'
    
    elif percentage < 90 and percentage > 80:
        print("{} got a B grade".format(name))
        grade[name] = 'B'
    
    elif percentage < 80 and percentage > 70:
        print("{} got C grade".format(name))
        grade[name] = 'C'
    
    elif percentage < 70 and percentage > 60:
        print("{} got D grade".format(name))
        grade[name] = 'D'
    
    else:
        print("{} got failed".format(name))
        grade[name] = 'F'


print(grade)