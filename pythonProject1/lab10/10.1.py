import json

with open('данные.json', 'r') as file:
    data = json.load(file)

for product in data['products']:
    name = product['name']
    price = product['price']
    weight = product['weight']
    available = "В наличии" if product['available'] else "Нет в наличии!"
    print(f"Название: {name}\nЦена: {price}\nВес: {weight}\n{available}\n")