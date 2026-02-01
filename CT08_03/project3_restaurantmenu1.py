food = {
    "burger": 67,
    "ice cream": 69,
    "chicken nuggets": 420,
    "wa-er": 61,
    "coke": 6.7,
}

for key, value in food.items():
    print(f"{key}: {value}")

dolla= int(input("How much money you have? :"))
eating = {}
print("Welcome to China shop where we sell fast food which is very delicious and very cheap too.")
item = input("What you want? :").lower().strip()


while item != "no more":

    if item in food:
        price = food[item]
        sure = input(f"You sure you want ah? The {item} costs {price} :").lower().strip()

        if sure == "yes":
            if item in eating:
                eating[item] = price + price
            else: 
                eating[item] = price
            

            if price > dolla:
                print("Bro, you no money and no job and no family and no house and no life and no budget and no life saving and no bank saving and no money in bank and no girlfriend and no friends and no freedom and no food and no drink and no worth and no experience in life and you cant even order this thing cos you no money!!!!!!!")
                del eating[item]
                dolla += price

            dolla -= price
            item = input("What else you want? :"). lower().strip()

        else: 
            print("Failure, you waste uncle's time, dont come here again!")
            item = input("What else you want? :"). lower().strip()

    else:   
        print("Haiyaa, here dont have this food, you cannot see ah!")
        item = input("What else you want? :"). lower().strip()


total = 0
for ordered, money in eating.items():
    print(f"{ordered}: {money}")
    total += money

    


print(f"Total cost is ${total}")
print(f"you left with ${dolla}")





        
    




        
            






