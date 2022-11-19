# Nome: Cindi de Paula Saicosque | Data: 04 de Outubro de 2022
schedule = []
date = []

while True:
    print('Choose the desired option:\n[1] - Insert new appointment\n[2] - List appointments\n[3] - Close')
    choice = input('Enter the number of choice: ')
    if choice == '1':
        print('[1] - Insert new appointment: ')
        name = input('Enter appointment name: ')
        day = int(input('Enter appointment day: '))
        if day < 1 or day > 31:
            print('Invalid format, try again')
            continue
        month = int(input('Enter the month of the appointment: '))
        if month < 1 or month > 12:
            print('Invalid format, try again')
            continue
        year = int(input('Enter the year of appointment: '))
        if year < 18:
            print('Invalid format, try again')
            continue
        subject = input('Enter the subject of the appointment: ')
        date = (f'Day: {day}\nMonth: {month}\nYear: {year}')
        schedule.append([name, date, subject])
    elif choice == '2':
        print('[2] - List appointments:\n')
        for i in len(schedule):
            print(f'{i + 1} \n- Appointment name: {schedule[i][0]}\n- Date of appointment: {schedule[i][1]}\n- Subject: {schedule[i][2]}')
    elif choice == '3':
        print('[3] - Close\nGood morning\nAnd in case I dont see ya\nGood afternoon\nGood evening\nAnd Good Night')
        break
    else:
        print('Invalid choice, please retype')
        continue
