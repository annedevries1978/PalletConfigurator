from classes import Pallet

pallet = Pallet()

pallet.choose_pallet_type()
index = int(input("Choose pallet type:")) - 1
pallet.set_pallet_type(index)

if index == 0:
    pallet.euro_pallet()
elif index == 1:
    pallet.blok_pallet()


print("Pallet type:", pallet.pallet_type)
print("Pallet length", pallet.pallet_length, "cm")
print("Pallet width:", pallet.pallet_width, "cm")