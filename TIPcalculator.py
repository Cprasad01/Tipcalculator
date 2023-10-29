print("welcome to the tip calculator")
bill=float(input("what was the total bill?RS"))
tip=float(input("how mucch tip would you like to give? 10,12,15 :"))
people=int(input('how many people split the bill?'))
tip_as_percentage=tip/100

total_tip_amount=bill*tip_as_percentage

total_bill=bill+total_tip_amount

bill_per_person=total_bill/people

final_amount="{:.2f}".format(bill_per_person)
print(f"each person should pay: RS{ final_amount }")