class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' специализируется на кухне {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' открыт!")


newRestaurant = Restaurant("Итальянский дворик", "итальянская")
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()

# Вывод:
# Итальянский дворик
# итальянская
# Ресторан 'Итальянский дворик' специализируется на кухне итальянская.
# Ресторан 'Итальянский дворик' открыт!