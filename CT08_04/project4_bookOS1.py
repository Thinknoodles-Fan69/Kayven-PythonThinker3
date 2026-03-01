things = {
    "notebook": 2.50,
    "pencil": 0.50,
    "pen": 1.25,
    "ruler": 1.50,
    "eraser": 0.50,
    "writing pad": 2.50,
    "marker": 2.00,
    "glue": 3.00,
    "calculator": 35.00
    }


take = {
    
}

temp_qty_cost = {
    "quantity": 0,
    "cost": 0
}

print("Welcome to store.")
for thing, value in things.items():
    print(f"{thing}: {value}")

print("---------------------------------------------")

thingy = input("What? :").lower().strip()

while thingy != "no more":

    if thingy in things:
        amount = input("how many? :")
        # print(things[thingy])
        price = things[thingy] * float(amount)
        confirm = input(f"{thingy}* {amount}: {price} . Sure? :").lower().strip()
        

        if confirm == "yes":
                take[thingy] = temp_qty_cost
                take[thingy]["quantity"] = amount
                take[thingy]["cost"] = price
                thingy = input("Anymore? :").lower().strip()
        
        else:
            print("mhm")
            thingy = input("Anymore? :").lower().strip()
    
    else:
        print("Nah")
        thingy = input("Anymore? :").lower().strip()


print("----------------------------------------------")
print("Things:")

total = 0
for thingssss, thingyss in take.items():
    print(f"{thingssss}: {thingyss}")
    total += thingyss["cost"]


print(f"Total is ${total}")






















