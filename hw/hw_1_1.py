day1 = input()
day2 = input()
day3 = input()

drink = []
drink.append([day1[0], int(day1[1:])])
drink.append([day2[0], int(day2[1:])])
drink.append([day3[0], int(day3[1:])])

result = '可'
total_coffee = 0
total_sugar = 0
for i in range(3):
    daily_coffee = 0
    daily_sugar = 0
    if drink[i][0] == 'B':
        daily_coffee += 50 * drink[i][1]
        daily_sugar += 10 * drink[i][1]
    elif drink[i][0] == 'M':
        daily_coffee += 20 * drink[i][1]
        daily_sugar += 30 * drink[i][1]
    if daily_coffee > 300 or daily_sugar > 60:
        result = '不可'
        
    total_coffee += daily_coffee
    total_sugar += daily_sugar

if  total_coffee > 700 or total_sugar > 150:
    result = '不可'
for i in range(3):
    if drink[i][1] > 99:
        result = '不可'

print(result) 