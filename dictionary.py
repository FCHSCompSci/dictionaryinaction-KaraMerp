# Kara Morgan
# dictionary project 9/17/18

order=[]
def make_shirt(s_id,size,color,design):
    shirt = {
        's_id' : shirt_id,
        'size' : size,
        'color' : color,
        'design' : design
        }
    return shirt

def make_customer(s_id,name):
    customer = {
        's_id' : shirt_id,
        'name' : name
        }
    return customer

shirt_id = 0

while True:
    user_input = input("Would you like to order a [s]hirt, [p]ickup or [e]xit? ")
    if user_input == "s":
        order_name = input("What is the name for the order? ")
        s_name = make_customer(shirt_id, order_name)
        shirt_id = shirt_id + 1
        shirt_size = input("What size would you like? ")
        shirt_color = input("What color would you like? ")
        shirt_design = input("What design would you like? ")
        whole = make_shirt(shirt_id, shirt_size, shirt_color, shirt_design)
          
    elif user_input == "p":
        pass
    elif user_input == "e":
        print("Bye!!!")
        break


