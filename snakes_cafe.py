menu = {
    "Appetizers" : ["Wings" , "Cookies", "Spring Rolls"],
    "Entrees" : ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
    "Desserts" : ["Ice Cream", "Cake", "Pie"],
    "Drinks" : ["Coffee", "Tea", "Unicorn Tears"]
}


print("**************************************")
print("**    Welcome to the Snakes Cafe!   **")
print("**    Please see our menu below.    **")
print("** To quit at any time, type 'quit' or 'exit' **")
print("**************************************")


for key, value in menu.items():
    print("")  
    print(key)
    print("----------")
    for item in value:
        print(item)


print("")        
print("**************************************")


orders = []


while True:
    order = input("** What would you like to order? ** ")
    if order == 'quit' or order == 'exit':
        break
    elif order in [item for sublist in menu.values() for item in sublist]:
        orders.append(order)
        count = orders.count(order)
        print(f"** {count} order of {order} have been added to your meal **")
    else:
        print("** Sorry, what you ordered is not on the menu. **")


print("**************************************")
print(f"Your order is: {orders}")
print("**************************************")
