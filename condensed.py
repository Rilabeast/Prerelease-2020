data = [[["BPCM", "BPSH", "RPSS", "RPLL", "YPLS", "YPLL", "RTMS", "RTML", "YTLM", "YTLL"], ["Compact", "Clam Shell", "RoboPhone - 5-inch screen and 64 GB memory", "RoboPhone - 6-inch screen and 256 GB memory", "Y-Phone Standard - 6-inch screen and 64 GB memory", "Y-Phone Deluxe - 6-inch screen and 128 GB memory", "RoboTab - 8-inch screen and 64 GB memory", "RoboTab - 10-inch screen and 128 GB memory", "Y-Tab Standard - 10-inch screen and 128 GB memory", "Y-Phone Deluxe - 10-inch screen and 256 GB memory"], [29.99, 49.99, 199.99, 499.99, 549.99, 649.99, 149.99, 299.99, 499.99, 599.99]], [["SMNO", "SMPG"], ["SIM Free (no SIM card purchased)", "Pay As You Go (SIM card purchased)"], [0, 9.99]], [["CSST", "CSLX"], ["Standard", "Luxury"], [0, 50]], [["CGCR", "CGHM", "CGCR][CGHM", "NONE"], ["Car", "Home", "Car + Home", "None"], [19.99, 15.99, 35.98, 0]]]
purchase = [[], [], [], []]
total, saved, discount, exit = 0, 0, 1, False
while not exit:
    subPurchase = [[], [], [], []]
    subtotal, x = 0, 0
    while x < len(data):
        print(["Devices", "SIM cards", "Cases", "Chargers"][x] + "\n---------------------------------------------\n" + "\n".join([("'{0}' : {1} (%.2f$)" .format(i, data[x][1][i]) % data[x][2][i]) for i in range(len(data[x][0]))]))
        choice = -1
        while choice < 0 or choice >= len(data[x][0]):
            try: choice = int(input("\nChoice: "))
            except ValueError: pass
        subtotal += data[x][2][choice]
        purchase[x].append(choice), subPurchase[x].append(choice), print("\n")
        x += 2 if (x == 0 and choice >= 6) else 1
    tempSaved, total, saved = subtotal * (1 - discount), total + subtotal * discount, saved + (subtotal * (1 - discount))
    [print("\n".join([("[{0}] {1} (%.2f$)" .format(data[x][0][i], data[x][1][i]) % data[x][2][i]) for i in subPurchase[x] if data[x][0][i] != "NONE"])) for x in range(len(subPurchase))]
    print("Subtotal: %.2f$" % (subtotal * discount) + "\nSaved: %.2f$" % tempSaved)
    discount, exit = 0.9, input("\ntype 'y' to order another device with a 10% discount or anything else to exit: ") != 'y'
    print("\n\n")
[print("\n".join([("[{0}] {1} (%.2f$)" .format(data[x][0][i], data[x][1][i]) % data[x][2][i]) for i in purchase[x] if data[x][0][i] != "NONE"])) for x in range(len(purchase))]
print("\nTotal: %.2f$" % total + "\nSaved: %.2f$" % saved)