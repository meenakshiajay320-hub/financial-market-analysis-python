
#menu for graph
import pandas as pd
import matplotlib.pyplot as plt
#intro
print("______________________________________________________________________________________________________________")
print("                                           BULL&BEAR METRICS                                                  ")
print("______________________________________________________________________________________________________________")
print(" ")
print("The stock market is designed to transfer money from the active to the patient")
print("                                                               -Warren Buffet")
print(" ")
print("WE PROVIDE DETAILS OF 20 STOCKS LISTED ON SEBI")
print("THE OPTIONS WE PROVIDE IN THIS STOCKVIEW PROGRAM ARE:\n -TO VIEW GRAPHS OF 5 COLOUMNS\n -TO VIEW COLOUMN-WISE DETAILS OF ALL STOCKS\n -TO PREDICT THE FUTURE TREND OF ALL STOCKS\n -TO VIEW RECOMMENDED STOCKS TO BUY BASED ON THE PIOTROSKI SCORE")
print("HERE IS THE LIST:")
print("______________________________________________________________________________________________________________")
#csv display
df=pd.read_csv("C:\Program Files\Python37\STOCK EXCHANGE 15.csv")
df.set_index("S.NO",inplace=True)
print(df)
print("______________________________________________________________________________________________________________")
print("MENU FOR GRAPH")
print("1.Price as on 13/10/2024")
print("2.Market Capital")
print("3.52 Week High price")
print("4.52 Week Low price")
print("5.365 day % change")
print("--------------------------------------------------------------------------------------------------------------")
#GRAPH1
ch=int(input("enter your choice"))
if ch==1:
    x=df["STOCK NAME"]
    y=df["PRICE"]
    plt.bar(x,y,width=0.3,color='c')
    plt.show()
#GRAPH2
elif ch==2:
    x=df["STOCK NAME"]
    y=df["MARKET CAPITAL"]
    plt.bar(x,y,width=0.3,color='c')
    plt.xlabel("STOCK NAME")
    plt.ylabel("MARKET CAPITAL")
    plt.show()
#GRAPH3
elif ch==3:
    x=df["STOCK NAME"]
    y=df["52 W H"]
    plt.xlabel("STOCK NAME")
    plt.ylabel("52 WEEK HIGH PRICE")
    plt.bar(x,y)
    plt.show()
#GRAPH4
elif ch==4:
    x=df["STOCK NAME"]
    y=df["52 W L"]
    plt.bar(x,y)
    plt.xlabel("STOCK NAME")
    plt.ylabel("52 WEEK LOW PRICE")
    plt.show()
#GRAPH5
elif ch==5:
    x=df["STOCK NAME"]
    y=df["365 D % CHANGE"]
    plt.bar(x,y)
    plt.xlabel("STOCK NAME")
    plt.ylabel("365 DAYS % CHANGE")
    plt.show()
else:
    print("INVALID CHOICE")
print("______________________________________________________________________________________________________________")
#NEXT
print("MORE DETAILED ANALYSIS:")
print("OPTIONS AVAILABLE")
print("1.view the sector of each stock")
print("2.view the price as on 13/10/2024 of all stocks")
print("3.view the market capital of all stocks")
print("4.view the 52 Week High Price of all stocks")
print("5.view the 52 Week Low Price of all stokcs")
print("6.view the 30 Day % change in price of all stocks")
print("7.view the 365 Day % change in price of all stocks")
print("8.view the P/E(Price to Equity) Ratio of all stocks")
print("9.view the ROE(Return on expenditure)of all stocks")
print("10.view the ROA(Return on Assets)of all stocks")
print("11.Predict the future trend of all stocks")
print("12.Recommendation of stock to buy based on piotroski score")
print("--------------------------------------------------------------------------------------------------------------")
#if statement
ch=int(input("ENTER A VALID OPTION NUMBER FROM ABOVE"))
if ch==1:
    print("SECTOR OF ALL STOCKS")
    print(df.iloc[:,[0,1]])
elif ch==2:
    print("PRICE OF STOCKS ON 13th OCTOBER 2024")
    print(df.iloc[:,[0,2]])
elif ch==3:
    print("MARKET CAPITAL OF ALL STOCKS")
    print(df.iloc[:,[0,3]])
    print("values in crores")
elif ch==4:
    print("52 WEEK HIGH PRICE OF STOCKS")
    print(df.iloc[:,[0,4]])
elif ch==5:
    print("52 WEEK LOW PRICE OF STOCKS")
    print(df.iloc[:,[0,5]])
elif ch==6:
    print("PERCENTAGE CHANGE OF STOCK PRICES IN 30 DAYS")
    print(df.iloc[:,[0,6]])
elif ch==7:
    print("PERCENTAGE CHANGE OF STOCK PRICES IN 365 DAYS")
    print(df.iloc[:,[0,7]])
elif ch==8:
    print("PRICE TO EQUITY(P/E) RATIO OF STOCKS")
    print(df.iloc[:,[0,8]])
elif ch==9:
    print("RETURN ON EXPENDITURE OF STOCKS")
    print(df.iloc[:,[0,9]])
elif ch == 10:
    print("RETURN ON ASSETS OF STOCKS")
    print(df.iloc[:,[0,10]])
elif ch==11: 
    if df["52 W H"].iloc[0] > df["52 W L"].iloc[0]:
        df["TREND"]="EXPECTED TO INCREASE"
    else:
        df["TREND"]="EXPECTED TO DECREASE"
    print("FUTURE TREND OF STOCK(INCREASE/DECREASE)")
    print(df["TREND"])
    print(' ')
    print("THIS PREDICTION IS BASED ON THE DIFFERENCES OF PRICE RANGE OF  52 WEEK HIGH AND LOW PRICE OF THE PARTICULAR\nSTOCKS EVENTHOUGH WE CANNOT PREDICT WHEN THE STOCK WILL ATTAIN THE PREDICTED OUTPUT,\n THIS WILL GIVE AN IDEA ABOUT THE FUTURE TREND OF THE STOCK")
elif ch==12:
    df.sort_values(by="PIOTROSKI",ascending=False,inplace=True)
    x=df[df["PIOTROSKI"]>6]
    y=pd.DataFrame(x)
    print("RECOMMENDATION STOCKS TO BUY BASED ON PIOTROSKI SCORE(7,8,9)")
    print(y.iloc[:,[0,11]])
    print(' ')
    print("STOCKS WITH PIOTRSOKI SCORE ABOVE 7 ARE GENERALLY CONSIDERED AS THE BEST TO BUY\n(PIOTROSKI SCORE IS CALCULATED AFTER EVALUATING 9 FUNDAMENTALS OF STOCKS)")
else:
    print("WE ARE EXTREMELY SORRY IT IS AN INVALID CHOICE!")
df.to_csv("C:\Program Files\Python37\STOCK EXCHANGE.csv")
print(" ")
print(" ")
print(" ")
print("______________________________________________________________________________________________________________")
print("Be fearful when others are greedy, and greedy when others are fearful")
print("                                                       -Warren Buffet")
print("______________________________________________________________________________________________________________")
print('©bull&bearmetrics')
