#
# Болница
# За даден период от време, всеки ден в болницата пристигат пациенти за преглед. Тя разполага първоначално със 7 лекари.
# Всеки лекар може да преглежда само по един пациент на ден, но понякога има недостиг на лекари, затова останалите
# пациенти се изпращат в други болници. Всеки трети ден, болницата прави изчисления и ако броят на непрегледаните
# пациенти е по-голям от броя на прегледаните, се назначава още един лекар. Като назначаването става преди да започне
# приемът на пациенти за деня.
# Напишете програма, която изчислява за дадения период броя на прегледаните и непрегледаните пациенти.
# Вход
# Входът се чете от конзолата и съдържа:
# На първия ред – периода, за който трябва да направите изчисления. Цяло число в интервала [1 ... 1000]
# На следващите редове(равни на броят на дните) – броя пациенти, които пристигат за преглед за
# текущия ден. Цяло число в интервала [0…10 000]
# Изход
# Да се отпечатат на конзолата 2 реда :
# На първия ред: "Treated patients: {брой прегледани пациенти}."
# На втория ред: "Untreated patients: {брой непрегледани пациенти}."
# Errors in judge, need to fix

num_days = int(input())
num_doctors = 7
treated_patients = 0
untreated_patients = 0

total_patients = 0

for day in range(1, num_days+1):
    today_patients = int(input())
    if today_patients > num_doctors:
        if day % 3 == 0:
            num_doctors += 1
        untreated_patients += today_patients - num_doctors
        treated_patients += num_doctors
    else:
        treated_patients += today_patients

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")

'''
period_days = int(input())
doctor_number = 7
total_threated_patients = 0
total_unthreated_patienst = 0

for i in range(1, period_days + 1):
    daily_threated_patients = 0
    daily_unthreated_patients = 0

    if i % 3 == 0 and total_unthreated_patienst > total_threated_patients:
        doctor_number += 1
    patients_count = int(input())

    if doctor_number >= patients_count:
        daily_threated_patients = patients_count
        daily_unthreated_patients = 0
    if doctor_number < patients_count:
        daily_unthreated_patients = patients_count - doctor_number
        daily_threated_patients = patients_count - daily_unthreated_patients

    total_threated_patients += daily_threated_patients
    total_unthreated_patienst += daily_unthreated_patients

print(f'Treated patients: {total_threated_patients}.')
print(f'Untreated patients: {total_unthreated_patienst}.')

'''