class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' специализируется на кухне {self.cuisine_type}. Рейтинг: {self.rating}")

    def update_rating(self, new_rating):
        self.rating = new_rating


restaurant1 = Restaurant("Итальянский дворик", "итальянская", 4.5)
restaurant2 = Restaurant("Пекин", "китайская", 3.9)
restaurant3 = Restaurant("Ботинки и грибы", "европейская", 4.1)

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

restaurant1.update_rating(4.8)
restaurant1.describe_restaurant()

# Вывод:
# Ресторан 'Итальянский дворик' специализируется на кухне итальянская. Рейтинг: 4.5
# Ресторан 'Пекин' специализируется на кухне китайская. Рейтинг: 3.9
# Ресторан 'Ботинки и грибы' специализируется на кухне европейская. Рейтинг: 4.1
# Ресторан 'Итальянский дворик' специализируется на кухне итальянская. Рейтинг: 4.8