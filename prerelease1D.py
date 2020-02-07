__author__ = "https://github.com/Rilabeast"
code = ["BPCM", "BPSH", "RPSS", "RPLL", "YPLS", "YPLL", "RTMS", "RTML", "YTLM", "YTLL", "SMNO", "SMPG", "CSST", "CSLX", "CGCR", "CGHM"]
desc = ["Compact", "Clam Shell", "RoboPhone - 5-inch screen and 64 GB memory", "RoboPhone - 6-inch screen and 256 GB memory", "Y-Phone Standard - 6-inch screen and 64 GB memory", "Y-Phone Deluxe - 6-inch screen and 128 GB memory", "RoboTab - 8-inch screen and 64 GB memory", "RoboTab - 10-inch screen and 128 GB memory", "Y-Tab Standard - 10-inch screen and 128 GB memory", "Y-Phone Deluxe - 10-inch screen and 256 GB memory", "SIM Free (no SIM card purchased)", "Pay As You Go (SIM card purchased)", "Standard", "Luxury", "Car", "Home"]
price = (29.99, 49.99, 199.99, 499.99, 549.99, 649.99, 149.99, 299.99, 499.99, 599.99, 0, 9.99, 0, 50, 19.99, 15.99)
pos = ((0, 10), (10, 12), (12, 14), (14, 16))
# 0-9 = dev, 10-11 = sim, 12-13 = case, 14-15 charger

purchase = [] # list of positions [devices], [sim], [case], [charger]
total = 0
saved = 0
discount = 1

exit = False
while not exit:
    subPurchase = []
    subtotal = 0
    p = 0
    while p < len(pos):
        [print("'{0}' : {1} ({2}$)" .format(i - pos[p][0], desc[i], price[i])) for i in range(pos[p][0], pos[p][1])]
        c = -1
        while c < pos[p][0] or c >= pos[p][1]:
            try:
                c = int(input("Choice: ")) + pos[p][0]
            except ValueError:
                pass
        subtotal += price[c]
        purchase.append(c)
        subPurchase.append(c)
        p += 2 if (p == 0 and c >= 6) else 1
        print()

    total += subtotal * discount
    saved += subtotal * (1 - discount)
    discount = 0.9
    print("\n")

    for i in subPurchase:
        print("[{0}] {1} ({2}$)" .format(code[i], desc[i], price[i]))

    exit = input("\n\ntype 'y' to order another device with a 10% discount or anything else to exit: ") != 'y'
    print("\n\n")

print()

for i in purchase:
    print("[{0}] {1} ({2}$)" .format(code[i], desc[i], price[i]))

print("\nTotal: %.2f$" % total)
print("Saved: %.2f$" % saved)

input("Press enter to exit...")