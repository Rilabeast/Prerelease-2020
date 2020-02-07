### 0478/21/PRE/M/J/20 ###
__author__ = "https://github.com/Rilabeast"
## creating variables to store everything ##
# variable that stores all of the data needed
data = [[["BPCM", "BPSH", "RPSS", "RPLL", "YPLS", "YPLL", "RTMS", "RTML", "YTLM", "YTLL"], # [code]
         ["Compact", "Clam Shell", "RoboPhone - 5-inch screen and 64 GB memory", "RoboPhone - 6-inch screen and 256 GB memory", "Y-Phone Standard - 6-inch screen and 64 GB memory", "Y-Phone Deluxe - 6-inch screen and 128 GB memory", "RoboTab - 8-inch screen and 64 GB memory", "RoboTab - 10-inch screen and 128 GB memory", "Y-Tab Standard - 10-inch screen and 128 GB memory", "Y-Phone Deluxe - 10-inch screen and 256 GB memory"], # description
         [29.99, 49.99, 199.99, 499.99, 549.99, 649.99, 149.99, 299.99, 499.99, 599.99]], # [price]
        # devices

        [["SMNO", "SMPG"], # [code]
         ["SIM Free (no SIM card purchased)", "Pay As You Go (SIM card purchased)"], # [description]
         [0, 9.99]], # [price]
        # SIM card options

        [["CSST", "CSLX"], # [code]
         ["Standard", "Luxury"], # [description]
         [0, 50]], # [price]
        # case options

        [["CGCR", "CGHM", "CGCR][CGHM", "NONE"], # [code]
         ["Car", "Home", "Car + Home", "None"], # [description]
         [19.99, 15.99, 35.98, 0]]] # [price]
        # charger options

purchase = [[], [], [], []] # list of indexes of all items bought: [devices], [sim], [case], [charger]
total = 0 # total cost
saved = 0 # total money saved
discount = 1 # discount, starts at 1 so that there is no decrease in price for first device

exit = False # variable for knowing whether the loop should repeat, repeats when it's false so initializing it as such so that it runs at least once
while not exit:
    subPurchase = [[], [], [], []] # 2D list for the indexes of the items bought: [devices], [sim], [case], [charger]
    subtotal = 0
    x = 0
    while x < len(data):
        for i in range(len(data[x][0])):
            print("'{0}' : {1} (%.2f$)" .format(i, data[x][1][i]) % data[x][2][i])
        print()
        choice = -1
        while choice < 0 or choice >= len(data[x][0]):
            try:
                choice = int(input("Choice: "))
            except ValueError:
                pass
        subtotal += data[x][2][choice]
        purchase[x].append(choice)
        subPurchase[x].append(choice)
        print()
        x += 1 if (x == 0 and choice >= 6) else 2

    tempSaved = subtotal * (1 - discount)
    total += subtotal * discount
    saved += tempSaved
    print()

    for x in range(len(subPurchase)):
        for i in subPurchase[x]:
            if data[x][0][i] != "NONE": print("[{0}] {1} (%.2f$)" .format(data[x][0][i], data[x][1][i]) % data[x][2][i])

    print("\nSubtotal: %.2f$" % (subtotal * discount))
    print("Saved: %.2f$" % tempSaved)

    discount = 0.9
    exit = input("\n\ntype 'y' to order another device with a 10% discount or anything else to exit: ") != 'y'
    print("\n\n")

print()
for x in range(len(purchase)):
    for i in purchase[x]:
        if data[x][0][i] != "NONE": print("[{0}] {1} (%.2f$)" .format(data[x][0][i], data[x][1][i]) % data[x][2][i])

print("\nTotal: %.2f$" % total)
print("Saved: %.2f$" % saved)