using System;
using System.Linq;
using System.Collections.Generic;

namespace PrereleaseCSharp
{
    class Program
    {
        // Made by github.com/Rilabeast
        static void Main()
        {
            string[] code = { "BPCM", "BPSH", "RPSS", "RPLL", "YPLS", "YPLL", "RTMS", "RTML", "YTLM", "YTLL", "SMNO", "SMPG", "CSST", "CSLX", "none", "CGCR", "CGHM", "15+16" };
            string[] desc = { "Compact", "Clam Shell", "RoboPhone - 5-inch screen and 64 GB memory", "RoboPhone - 6-inch screen and 256 GB memory", "Y-Phone Standard - 6-inch screen and 64 GB memory", "Y-Phone Deluxe - 6-inch screen and 128 GB memory", "RoboTab - 8-inch screen and 64 GB memory", "RoboTab - 10-inch screen and 128 GB memory", "Y-Tab Standard - 10-inch screen and 128 GB memory", "Y-Phone Deluxe - 10-inch screen and 256 GB memory", "SIM Free (no SIM card purchased)", "Pay As You Go (SIM card purchased)", "Standard", "Luxury", "No Charger", "Car", "Home", "Car + Home" };
            float[] price = { 29.99f, 49.99f, 199.99f, 499.99f, 549.99f, 649.99f, 149.99f, 299.99f, 499.99f, 599.99f, 0f, 9.99f, 0f, 50f, 0f, 19.99f, 15.99f, 35.98f };
            int[] pos = { 0, 10, 10, 12, 12, 14, 14, 18 }; // 0-9 = dev, 10-11 = sim, 12-13 = case, 14-17 charger; n*2 -> (n*2)+1

            List<int> purchase = new List<int>(); // list of positions of chosen items
            float total = 0; // total price
            float saved = 0; // total amount saved
            float discount = 1; // discount multiplier

            string[] types = { "Devices", "SIM cards", "Cases", "Chargers" };

            bool exit = false;
            while (!exit)
            {
                List<int> subPurchase = new List<int>();
                float subtotal = 0;
                float tempSaved = 0;
                int p = 0;
                while (p < (pos.Length / 2))
                {
                    Console.WriteLine($"\n{types[p]}\n---------------------------------------------\n");
                    for (int i = 0; i < (pos[(p * 2) + 1] - pos[p * 2]); i++)
                    {
                        Console.WriteLine($"'{i}' : {desc[i]} ({price[i]}$)");
                    }
                    Console.WriteLine();

                    int c = -1;
                    while (c < pos[p * 2] || c >= (pos[(p * 2) + 1]))
                    {
                        try
                        {
                            Console.Write("Choice: ");
                            c = Convert.ToInt32(Console.ReadLine()) + (pos[p * 2]);
                        }
                        catch (System.Exception) { }
                    }

                    if (code[c] != "none")
                    {
                        subtotal += price[c] * (p == 0 ? discount : 1);
                        tempSaved += price[c] * (1 - (p == 0 ? discount : 1));

                        if (p == 0)
                        {
                            saved += (price[c] * (1 - discount));
                        }

                        if (code[c].Contains('+'))
                        {
                            foreach (string i in code[c].Split('+'))
                            {
                                int temp = Convert.ToInt32(i);
                                purchase.Add(temp);
                                subPurchase.Add(temp);
                            }
                        }
                        else
                        {
                            purchase.Add(c);
                            subPurchase.Add(c);
                        }
                    }
                    p += (p == 0 && c >= 6) ? 2 : 1;
                    Console.WriteLine();
                }

                total += subtotal;
                saved += tempSaved;
                discount = 0.9f;

                Console.WriteLine("\n");
                foreach (int i in subPurchase)
                {
                    Console.WriteLine($"[{code[i]}] {desc[i]} ({price[i]}$)");
                }
                Console.WriteLine($"\nSubtotal: {Math.Round(subtotal, 2)}$" + (tempSaved != 0 ? ($"\nSaved: {Math.Round(tempSaved, 2)}$") : ""));

                Console.Write("\n\ntype 'y' to order another device with a 10% discount or anything else to exit: ");
                exit = Console.ReadLine() != "y";
                Console.WriteLine("\n");
            }

            Console.WriteLine("\n\n");
            foreach (int i in purchase)
            {
                Console.WriteLine($"[{code[i]}] {desc[i]} ({price[i]}$)");
            }

            Console.WriteLine($"\nTotal: {Math.Round(total, 2)}$");
            Console.WriteLine($"Saved: {Math.Round(total, 2)}$");

            Console.Write("Press anything to exit... ");
            Console.ReadKey();
        }
    }
}
