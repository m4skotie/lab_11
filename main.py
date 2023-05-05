def  z1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"Название ресторана {self.restaurant_name}, Кухня:{self.cuisine_type}")
        def open_restaurant(self):
            print("Ресторан сейчас открыт.")
    newRestaurant = Restaurant("Burger king", "Американская")
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()
def  z2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"Название ресторана {self.restaurant_name}, Кухня:{self.cuisine_type}")
        def open_restaurant(self):
            print("Ресторан сейчас открыт.")
    name = input("Введите название ресторана: ")
    cuisin = input("Введите кухню: ")
    newRestoraunt = Restaurant(name, cuisin)
    print(newRestoraunt.restaurant_name)
    print(newRestoraunt.cuisine_type)
    newRestoraunt.describe_restaurant()
    newRestoraunt.open_restaurant()

def z3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating
        def describe_restaurant(self):
            print(f"Название ресторана {self.restaurant_name}, Кухня:{self.cuisine_type}, Рейтинг:{self.rating}")
    newRestaurant = Restaurant("Burger king", "Американская", "8/10")
    newRestaurant.describe_restaurant()
    newRestaurant.rating=input("Введите новый рейтинг: ")
    newRestaurant.describe_restaurant()
z3()
