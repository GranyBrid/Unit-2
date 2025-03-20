


class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

def main():
    restaurant_one = Restaurant("restaurant","mexican")
    restaurant_two = Restaurant("Burger Guy","american")
    restaurant_three = Restaurant("Chicken Place","japanese")
    print(f"The restaurant is called {restaurant_one.restaurant_name}")
    print(f"The restaurant serves {restaurant_one.cuisine_type} food")

    restaurant_one.describe_restaurant()
    restaurant_one.open_restaurant()
    print("")
    restaurant_two.describe_restaurant()
    restaurant_three.describe_restaurant()

if __name__ == "__main__":
    main()

class User:
    def __init__(self, first_name: str, last_name: str, username: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}'s username is {self.username}, and they are {self.age} years old.")
    
    def greet_user(self):
        print(f"Hello {self.username}, or {self.first_name}!")

def main2():
    user_one = User("Jimmy","Jimmy","Antavius",16)
    user_two = User("Logan","Rheni","WackyWho",3)
    user_three = User("Real","Name","Gaster",15)

    print("")
    user_one.describe_user()
    user_one.greet_user()
    print("")
    user_two.describe_user()
    user_two.greet_user()
    print("")
    user_three.describe_user()
    user_three.greet_user()

if __name__ == "__main__":
    main2()
