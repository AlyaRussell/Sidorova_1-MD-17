class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' специализируется на кухне {self.cuisine_type}.")


restaurant1 = Restaurant("Итальянский дворик", "итальянская")
restaurant2 = Restaurant("Пекин", "китайская")
restaurant3 = Restaurant("Ботинки и грибы", "европейская")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# Вывод:
# Ресторан 'Итальянский дворик' специализируется на кухне итальянская.
# Ресторан 'Пекин' специализируется на кухне китайская.
# Ресторан 'Ботинки и грибы' специализируется на кухне европейская.