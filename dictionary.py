#Kara Morgan
#Dictionary 9/18/18

Hoody = []
shirt = []
tanktop = []

order = input("Would you like to place a order?: ")

if order == "no":
    print("Bye!")
else:
    print("For a Hoodie use the first funtion, for a Shirt use the second function, and for a Tanktop use the third function. ")
    
    def first(size, color, design):
        Hoody={
            'size' : size,
            'color' : color,
            'design' : design
            }
        hoody.append(Hoody)
        return "Thank you for your Hoodie order" 


    def second(size, color, design):
        shirt={
            'size' : size,
            'color' : color,
            'design' : design
            }
        shirt.append(shirt)
        return "thank you for your Shirt order"

    def third(size, color, design):
        tanktop={
            'size' : size,
            'color' : color,
            'design' :  design
            }
        tanktop.append(tanktop)
        return "Thank you for your Tanktop order"

orders = Hoody + shirt + tanktop
print(orders)


