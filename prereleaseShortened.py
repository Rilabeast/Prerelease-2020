data = [[["BPCM", "BPSH", "RPSS", "RPLL", "YPLS", "YPLL", "RTMS", "RTML", "YTLM", "YTLL"],
         ["Compact", "Clam Shell", "RoboPhone - 5-inch screen and 64 GB memory", "RoboPhone - 6-inch screen and 256 GB memory", "Y-Phone Standard - 6-inch screen and 64 GB memory", "Y-Phone Deluxe - 6-inch screen and 128 GB memory", "RoboTab - 8-inch screen and 64 GB memory", "RoboTab - 10-inch screen and 128 GB memory", "Y-Tab Standard - 10-inch screen and 128 GB memory", "Y-Phone Deluxe - 10-inch screen and 256 GB memory"],
         [29.99, 49.99, 199.99, 499.99, 549.99, 649.99, 149.99, 299.99, 499.99, 599.99]],

         [["SMNO", "SMPG"],
         ["SIM Free (no SIM card purchased)", "Pay As You Go (SIM card purchased)"],
         [0, 9.99]],

         [["CSST", "CSLX"],
         ["Standard", "Luxury"],
         [0, 50]],

         [["CGCR", "CGHM", "CGCR][CGHM", "NONE"],
         ["Car", "Home", "Car + Home", "None"],
         [19.99, 15.99, 35.98, 0]]]


purchase = [[], [], [], []] # list of positions [devices], [sim], [case], [charger]
total = 0
saved = 0
discount = 1

exit = False
while not exit:
    subPurchase = [[], [], [], []]
    subtotal = 0
    for x in range(len(data)):
        for i in range(len(data[x][0])):
            print("'{0}' : {1} ({2}$)" .format(i, data[x][1][i], data[x][2][i]))
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

    tempSaved = subtotal * (1 - discount)
    total += subtotal * discount
    saved += tempSaved
    print()

    for i in range(len(subPurchase)):
        for x in subPurchase[i]:
            if data[x][0][i] != "NONE": print("[{0}] {1} ({2}$)" .format(data[i][0][x], data[i][1][x], data[i][2][x]))

    print("\nSubtotal: %.2f$" % (subtotal * discount))
    if tempSaved != 0: print("Saved: %.2f$" % tempSaved)

    discount = 0.9
    exit = input("\n\ntype 'y' to order another device with a 10% discount or anything else to exit: ") != 'y'
    print("\n\n")

print()
for x in range(len(purchase)):
    for i in purchase[x]:
        if data[x][0][i] != "NONE": print("[{0}] {1} (%.2f$)" .format(data[x][0][i], data[x][1][i]) % data[x][2][i])

print("\nTotal: %.2f$" % total)
print("Saved: %.2f$" % saved)