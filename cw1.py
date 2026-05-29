import random
apple_juice = 15.5
orange_juice = 20
grape_juice = 10.25
total_vol = apple_juice + orange_juice + grape_juice
print("Total volume sold:", total_vol, "liters")
total_vol= int(total_vol);
print("Total volume as integer:",total_vol)
total_vol=str(total_vol)
print("Total volume of juice sold is", total_vol, "litres")
bonus_litres = random.randint(5,10)
total_vol= int(total_vol)
final_total = total_vol + bonus_litres
print("Bonus Litres added:",bonus_litres)
print("Final total volume is",final_total,"litres")