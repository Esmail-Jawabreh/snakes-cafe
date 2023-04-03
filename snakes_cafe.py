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
    if order == 'quit':
        break
    elif order == 'exit':
        break
    elif order in [item for sublist in menu.values() for item in sublist]:
        orders.append(order)
        print(f"** {len(orders)} order of {order} have been added to your meal **")
    else:
        print("** Sorry, what your ordered is not on the menu. **")


print("**************************************")
print(f"Your order is: {orders}")
print("**************************************")
