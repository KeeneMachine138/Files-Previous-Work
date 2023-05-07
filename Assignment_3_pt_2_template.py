num_bags = int(input("Input the number of bags: "))
ticket_type = input("Input ticket type: ")
bag_fee = 0
if ticket_type == "first-class":
    base_ticket_price = 1000
    if num_bags <= 5:
        bag_fee = 0
    else:
        # remember the first 5 bags are free
        bag_fee = (num_bags-5) * 20
elif ticket_type == "business-class":
    base_ticket_price = 750

else:
    base_ticket_price = 500

total_ticket_price = bag_fee + base_ticket_price
total_ticket_price = float(total_ticket_price)
print("Passenger total ticket price is: ${0:.2f}".format(total_ticket_price))
