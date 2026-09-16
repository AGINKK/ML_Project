cars = []
print("--- Enter Details for 3 Cars ---")

for i in range(1, 4):
    print(f"\nCar #{i}:")
    brand = input("Enter brand: ")
    model = input("Enter model: ")
    price = int(input("Enter price: "))  
    
   
    new_car = {"brand": brand, "model": model, "price": price}
    cars.append(new_car)

# 3. Display the stored information
print("\n--- Stored Car Inventory ---")
for index, car in enumerate(cars, start=1):
    print(f"Car {index}: {car['brand']} {car['model']} | Price: {car['price']:,}")
