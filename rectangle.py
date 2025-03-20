class Rectangle:

    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        
def main():
    instance_one = Rectangle(3,4)
    print(instance_one.length, instance_one.width)

if __name__ == "__main__":
    main()