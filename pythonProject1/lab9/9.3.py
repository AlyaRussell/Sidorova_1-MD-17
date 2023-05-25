import csv

total_cost = 0

with open('../data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        product = row[0]
        quantity = int(row[1])
        price = int(row[2])
        total_cost += quantity * price
        print(f"{product} - {quantity} шт. за {price} руб.")

print(f"Итоговая сумма: {total_cost} руб.")