import questionary
# 5 Stocks Closing Price Overall Change
ABNB_day1close = 139.15
ABNB_day30close = 209.86
ABNB_overallchange = ((ABNB_day30close - ABNB_day1close) / ABNB_day1close) * 100
#If we wanted to print the overall Change
#print(f"The overall change for AirBNB is {round(ABNB_overallchange,2)}%")
DASH_day1close = 139.19
DASH_day30close = 212.17
DASH_overallchange = ((DASH_day30close - DASH_day1close) / DASH_day1close) * 100
#If we wanted to print the overall Change
#print(f"The overall change for DoorDash is {round(DASH_overallchange,2)}%")
PRCH_day1close = 13.37
PRCH_day30close = 22.36
PRCH_overallchange = ((PRCH_day30close - PRCH_day1close) / PRCH_day1close) * 100
#If we wanted to print the overall Change
#print(f"The overall change for Porch Group is {round(PRCH_overallchange,2)}%")
SNOW_day1close = 278.24
SNOW_day30close = 294.55
SNOW_overallchange = ((SNOW_day30close - SNOW_day1close) / SNOW_day1close) * 100
#If we wanted to print the overall Change
#print(f"The overall change for Snowflake is {round(SNOW_overallchange,2)}%")
UPST_day1close = 43.99
UPST_day30close = 92.27
UPST_overallchange = ((UPST_day30close - UPST_day1close) / UPST_day1close) * 100
#If we wanted to print the overall Change
#print(f"The overall change for Upstart is {round(UPST_overallchange,2)}%")
# Currency Value Overall Change
BRL_day1value = 0.133714
BRL_finaldayvalue = 0.12899
BRL_overallchange = ((BRL_finaldayvalue - BRL_day1value) / BRL_day1value) * 100
#If we wanted to print the overall Change
#PRCHprint(f"The overall change for the Brazilian Real is {round(BRL_overallchange,2)}%")
CAD_day1value = 0.541318
CAD_finaldayvalue = 0.545911
CAD_overallchange = ((CAD_finaldayvalue - CAD_day1value) / CAD_day1value) * 100
#If we wanted to print the overall Change
#print(f"The overall change for the Canadian Dollar is {round(CAD_overallchange,2)}%")
CLP_day1value = 0.000970862
CLP_finaldayvalue = 0.000963789
CLP_overallchange = ((CLP_finaldayvalue - CLP_day1value) / CLP_day1value) * 100
#If we wanted to print the overall Change
#print(f"The overall change for the Chilean Peso is {round(CLP_overallchange,2)}%")
EUR_day1value = 0.848712
EUR_finaldayvalue = 0.840823
EUR_overallchange = ((EUR_finaldayvalue - EUR_day1value) / EUR_day1value) * 100
#If we wanted to print the overall Change
#print(f"The overall change for the Euro is {round(EUR_overallchange,2)}%")
JPY_day1value = 0.0066961
JPY_finaldayvalue = 0.00656522
JPY_overallchange = ((JPY_finaldayvalue - JPY_day1value) / JPY_day1value) * 100
#If we wanted to print the overall Change
#print(f"The overall change for the Japanese Yen is {round(JPY_overallchange,2)}%")
# Create Dictionaries for each stock and each currency to be used in the interactive user application below.
tickers = {'DASH':DASH_overallchange, 'PRCH':PRCH_overallchange, 'ABNB':ABNB_overallchange, 'SNOW':SNOW_overallchange, 'UPST':UPST_overallchange}
currencies = {'BRL':BRL_overallchange, 'CAD':CAD_overallchange, 'CLP':CLP_overallchange, 'EUR':EUR_overallchange, 'JPY':JPY_overallchange}
# Stocks. This Questionary will determine which stock is a good investment. To do this we will only consider stocks that had their closing price increase by 25% or more.
answer = questionary.text("Out of DASH, PRCH, ABNB, SNOW, or UPST what company would you like to invest in?").ask()
if answer in tickers.keys():
    if tickers[answer] >= 25:
        print("Yes, this company is a good investment.")
    else:
        print("No, this company is not a good investment.")
else:
    print("No data for that company.")
# Currency. This Questionary will determine which Currency is good to investment with. To do this we will only consider currencies that did not devalue during the 30 day period.
answer2 = questionary.text("Out of BRL, CAD, CLP, EUR, or JPY what currency would you like to invest with?").ask()
if answer2 in currencies.keys():
    if currencies[answer2] >= 0:
        print("Yes, this currency makes sense to invest in.")
    else:
        print("No, this currency devalued and does not prove good to invest with.")
else:
    print("No data for that currency.")
