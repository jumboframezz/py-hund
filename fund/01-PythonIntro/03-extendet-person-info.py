'''
3. Extended Person Info
Write a Python program, which reads information about a person in the same format as the previous problem, and
prints it back to the console with the following format:
Name: {name}
Age: {age}
Town: {town}
Salary: ${salary}
Age range: {ageRange}
Salary range: {salaryRange}
Format the salary to the 2 nd decimal point.
The age range is as follows:
 If the person is less than 18 years old, they are a “teen”
 If the person is less than 70 years old, they are an “adult”
 Otherwise, the person is an “elder”
The salary range is as follows:
 If the salary is less than $500, it is “low”
 If the salary is less than $2000, it is “medium”
 Otherwise, the salary is “high”
Gosho
20
Sofia
530

'''

name=input()
age=int(input())
town=input()
salary=float(input())

if age <= 18:
    age_range = "teen"
elif age <= 70:
    age_range = "adult"
elif age > 70:
    age_range = "elder"

if salary <= 500:
    salary_range="low"
elif salary <= 2000:
    salary_range = "medium"
else:
    salary_range = "high"

print(f"Name: {name}\nAge: {age}\nTown: {town}\nSalary: ${salary:.2f}")
print(f"Age range: {age_range}\nSalary range: {salary_range}")

