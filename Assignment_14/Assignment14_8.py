class Vehicle:
    def start(self):
        print("Vehicle is starting...")

class Car(Vehicle):
    def start(self):
        print("Car is Starting...")


def main():

    V = Vehicle()
    V.start()

    C = Car()
    C.start()


if __name__ =="__main__":
    main()