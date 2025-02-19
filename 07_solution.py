order_size = "Medium"
extra_shot = False

if extra_shot:
    tea = order_size + " Coffee with an extra shoot"
else:
    tea = order_size + " coffee"

print("Order: ", tea)