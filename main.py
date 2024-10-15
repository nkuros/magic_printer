import os, random, sys
# from escpos.printer import Network

used_cards = []

while True:
    mana_count=input("Enter mana count or q to end program: ")
    if mana_count == "q":
        sys.exit()
    source = "./img/" + mana_count
    random_file=random.choice(os.listdir(source))
    if random_file not in used_cards:
        print("%d} printing %s"%(i+1,random_file))
        # p = Network("192.168.1.100") #Printer IP Address
        # p.image(random_file)
        # p.cut()
        used_cards.append(random_file)



# Some Handy examples:

# from escpos.printer import Usb
# p = Usb(0x04b8, 0x0202, 0, profile="TM-T88III")
# p.text("Hello World\n")
# p.image("logo.gif")
# p.cut()

# from escpos.printer import Network

# kitchen = Network("192.168.1.100") #Printer IP Address
# kitchen.text("Hello World\n")
# kitchen.barcode('4006381333931', 'EAN13', 64, 2, '', '')
# kitchen.cut()

