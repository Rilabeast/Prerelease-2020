__author__ = "https://github.com/Rilabeast"
devices = [["BPCM", "BPSH", "RPSS", "RPLL", "YPLS", "YPLL", "RTMS", "RTML", "YTLM", "YTLL"],
           ["Compact", "Clam Shell", "RoboPhone - 5-inch screen and 64 GB memory", "RoboPhone - 6-inch screen and 256 GB memory", "Y-Phone Standard - 6-inch screen and 64 GB memory", "Y-Phone Deluxe - 6-inch screen and 128 GB memory", "RoboTab - 8-inch screen and 64 GB memory", "RoboTab - 10-inch screen and 128 GB memory", "Y-Tab Standard - 10-inch screen and 128 GB memory", "Y-Phone Deluxe - 10-inch screen and 256 GB memory"],
           [29.99, 49.99, 199.99, 499.99, 549.99, 649.99, 149.99, 299.99, 499.99, 599.99]] # [code], [description], [price]

sim = [["SMNO", "SMPG"],
       ["SIM Free (no SIM card purchased)", "Pay As You Go (SIM card purchased)"],
       [0, 9.99]] # [code], [description], [price]

case = [["CSST", "CSLX"],
        ["Standard", "Luxury"],
        [0, 50]] # [code], [description], [price]

charger = [["CGCR", "CGHM"],
           ["Car", "Home"],
           [19.99, 15.99]] # [code], [description], [price]


purchase = [[], [], [], []] # list of positions [devices], [sim], [case], [charger]
total = 0
saved = 0
discount = 1

exit = False
while not exit:
    subPurchase = [[], [], [], []]
    subtotal = 0

    for i in range(len(devices[0])):
        print("'{0}' : {1} ({2}$)" .format(i, devices[1][i], devices[2][i]))
    print()
    devChoice = -1
    while devChoice < 0 or devChoice >= len(devices[0]):
        try:
            devChoice = int(input("Choice: "))
        except ValueError:
            pass
    subtotal += devices[2][devChoice]
    purchase[0].append(devChoice)
    subPurchase[0].append(devChoice)
    print()

    if devChoice < 6:
        for i in range(len(sim[0])):
            print("'{0}' : {1} ({2}$)" .format(i, sim[1][i], sim[2][i]))
        print()
        simChoice = -1
        while simChoice < 0 or simChoice >= len(case[0]):
            try:
                simChoice = int(input("Choice: "))
            except ValueError:
                pass
        subtotal += sim[2][simChoice]
        purchase[1].append(simChoice)
        subPurchase[1].append(simChoice)
        print()

    for i in range(len(case[0])):
        print("'{0}' : {1} ({2}$)" .format(i, case[1][i], case[2][i]))
    print()
    caseChoice = -1
    while caseChoice < 0 or caseChoice >= len(case[0]):
        try:
            caseChoice = int(input("Choice: "))
        except ValueError:
            pass
    subtotal += case[2][caseChoice]
    purchase[2].append(caseChoice)
    subPurchase[2].append(caseChoice)
    print()

    print("'0' : Car (19.99$)\n'1' : Home (15.99$)\n'2' : Both (35.98$)\n'3' : None (0$)")
    print()
    chargerChoice = -1
    while chargerChoice < 0 or chargerChoice >= 4:
        try:
            chargerChoice = int(input("Choice: ")) # 0 for car, 1 for home, 2 for both, 3 for neither
        except ValueError:
            pass
    if chargerChoice == 0 or chargerChoice == 2:
        subtotal += charger[2][0]
        purchase[3].append(0)
        subPurchase[3].append(0)
    if chargerChoice == 1 or chargerChoice == 2:
        subtotal += charger[2][1]
        purchase[3].append(1)
        subPurchase[3].append(1)

    total += subtotal * discount
    saved += subtotal * (1 - discount)
    discount = 0.9
    print("\n")

    for i in subPurchase[0]:
        print("[{0}] {1} ({2}$)" .format(devices[0][i], devices[1][i], devices[2][i]))

    for i in subPurchase[1]:
        print("[{0}] {1} ({2}$)" .format(sim[0][i], sim[1][i], sim[2][i]))

    for i in subPurchase[2]:
        print("[{0}] {1} ({2}$)" .format(case[0][i], case[1][i], case[2][i]))

    for i in subPurchase[3]:
        print("[{0}] {1} ({2}$)" .format(charger[0][i], charger[1][i], charger[2][i]))

    exit = input("\n\ntype 'y' to order another device with a 10% discount or anything else to exit: ") != 'y'
    print("\n\n")

print()

for i in purchase[0]:
    print("[{0}] {1} ({2}$)" .format(devices[0][i], devices[1][i], devices[2][i]))

for i in purchase[1]:
    print("[{0}] {1} ({2}$)" .format(sim[0][i], sim[1][i], sim[2][i]))

for i in purchase[2]:
    print("[{0}] {1} ({2}$)" .format(case[0][i], case[1][i], case[2][i]))

for i in purchase[3]:
    print("[{0}] {1} ({2}$)" .format(charger[0][i], charger[1][i], charger[2][i]))

print("\nTotal: %.2f$" % total)
print("Saved: %.2f$" % saved)