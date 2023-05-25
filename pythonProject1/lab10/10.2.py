import json

data = {}

try:
    with open('данные.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    data['products'] = []

while True:
    name = input("Введите название продукта (или q для выхода): ")
    if name.lower() == 'q':
        break
    price = int(input("Введите цену продукта: "))
    weight = int(input("Введите вес в граммах: "))
    available = input("Продукт в наличии? (y/n): ").lower() == 'y'
    product = {
        'name': name,
        'price': price,
        'weight': weight,
        'available': available
    }
    data['products'].append(product)

    with open('данные.json', 'w') as file:
        json.dump(data, file, indent=2)

    print("Продукт добавлен в список.")

print("\nСписок продуктов:")
for product in data['products']:
    name = product['name']
    price = product['price']
    weight = product['weight']
    available = "В наличии" if product['available'] else "Нет в наличии!"
    print(f"Название: {name}\nЦена: {price}\nВес: {weight}\n{available}\n")