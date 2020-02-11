__author__ = "https://github.com/Rilabeast"
code = ("BPCM", "BPSH", "RPSS", "RPLL", "YPLS", "YPLL", "RTMS", "RTML", "YTLM", "YTLL", "SMNO", "SMPG", "CSST", "CSLX", None, "CGCR", "CGHM", "15+16") # item codes
desc = ("Compact", "Clam Shell", "RoboPhone - 5-inch screen and 64 GB memory", "RoboPhone - 6-inch screen and 256 GB memory", "Y-Phone Standard - 6-inch screen and 64 GB memory", "Y-Phone Deluxe - 6-inch screen and 128 GB memory", "RoboTab - 8-inch screen and 64 GB memory", "RoboTab - 10-inch screen and 128 GB memory", "Y-Tab Standard - 10-inch screen and 128 GB memory", "Y-Phone Deluxe - 10-inch screen and 256 GB memory", "SIM Free (no SIM card purchased)", "Pay As You Go (SIM card purchased)", "Standard", "Luxury", "No Charger", "Car", "Home", "Car + Home") # item descriptions
price = (29.99, 49.99, 199.99, 499.99, 549.99, 649.99, 149.99, 299.99, 499.99, 599.99, 0, 9.99, 0, 50, 0, 19.99, 15.99, 35.98) # item prices
pos = ((0, 10), (10, 12), (12, 14), (14, 18)) # 0-9 = dev, 10-11 = sim, 12-13 = case, 14-17 charger

purchase = [] # list of positions of chosen items
total = 0 # total price
saved = 0 # total amount saved
discount = 1 # discount multiplier

exit = False
while not exit:
    subPurchase = []
    subtotal = 0
    tempSaved = 0
    p = 0
    while p < len(pos):
        print("\n" + ["Devices", "SIM cards", "Cases", "Chargers"][p] + "\n---------------------------------------------\n" + "\n".join(["'{0}' : {1} ({2}$)" .format(i - pos[p][0], desc[i], price[i]) for i in range(pos[p][0], pos[p][1])]))
        c = -1
        while c < pos[p][0] or c >= pos[p][1]:
            try: c = int(input("Choice: ")) + pos[p][0]
            except ValueError: pass
        if code[c] != None:
            subtotal += price[c] * (discount if p == 0 else 1)
            tempSaved += price[c] * (1 - (discount if p == 0 else 1))
            if p == 0: saved += price[c] * (1 - discount)
            if "+" in code[c]:
                for i in code[c].split("+"):
                    purchase.append(int(i))
                    subPurchase.append(int(i))
            else:
                purchase.append(c)
                subPurchase.append(c)
        p += 2 if (p == 0 and c >= 6) else 1
        print()

    total += subtotal
    saved += tempSaved
    discount = 0.9

    print("\n" + "\n".join(["[{0}] {1} ({2}$)" .format(code[i], desc[i], price[i]) for i in subPurchase]) + "\nSubtotal: %.2f$" % subtotal + (("\nSaved: %.2f$" % tempSaved) if tempSaved != 0 else ""))

    exit = input("\n\ntype 'y' to order another device with a 10% discount or anything else to exit: ") != 'y'
    print("\n")

print("\n" + "\n".join(["[{0}] {1} ({2}$)" .format(code[i], desc[i], price[i]) for i in purchase]))

print("\nTotal: %.2f$" % total)
print("Saved: %.2f$" % saved)

input("Press enter to exit...")