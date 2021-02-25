import questionary
#stocks
answer = questionary.text("Out of DASH, PRCH, ABNB, SNOW or UPST, what company would you like to invest in?").ask()

if answer == 'ABNB':
    print("Yes, this company is available for investment.")
elif answer == 'DASH':
    print("Yes, this company is available for investment.")
elif answer == 'PRCH':
    print("Yes, this company is available for investment.")
elif answer == 'SNOW':
    print("Yes, this company is available for investment.")
elif answer == 'UPST':
    print("Yes, this company is available for investment.")
else:
    print("No data for that company.")    

#currency
answer2 = questionary.text("Out of CAD, BRL, CLP, JPY, EUR, what currency would you like to invest with?").ask()

if answer2 == 'CAD':
    print("The value of this currency improved. Therefore, it's a good opportunity to invest.")
elif answer2 == 'BRL':
    print("The value of this currency improved. Therefore, it's a good opportunity to invest.")
elif answer2 == 'CLP':
    print("The value of this currency improved. Therefore, it's a good opportunity to invest.")
elif answer2 == 'JPY':
    print("The value of this currency improved. Therefore, it's a good opportunity to invest.")
elif answer2 == 'EUR':
    print("The value of this currency improved. Therefore, it's a good opportunity to invest.")
else:
    print("No data for that currency.")   