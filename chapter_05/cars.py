cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw': #if car is bmw, print in upper case
        print(car.upper())
    else: #else print in title case
        print(car.title())
print("\n")

car1 = 'bmw' #sets value of car1 to bmw
print(car1 == 'bmw') #checks if car1 is equal to bmw, returns True

car2 = 'bmw' #sets value of car2 to bmw
print(car2 == 'subaru') #checks if car2 is equal to bmw, returns False

car3 = 'bmw' #sets value of car3 to bmw
print(car3 == 'BMW') #checks if car3 is equal to BMW
#returns False since equality checks are **case-sensitive**

car4 = 'BMW' #sets value of car4 to BMW
print(car4.lower() == 'bmw') #checks if car4 is equal to BMW in lowercase
#returns True
print(car4) #.lower() doesn't change the original value