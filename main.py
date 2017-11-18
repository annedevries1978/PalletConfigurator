#!python3
"""
A simple pallet configurator to find the optimum numbers of boxes per layer
Learn to work witch classes and maybe also so something with property
TODO: implement optimum pallet layer config optimisation
"""
from classes import Pallet, Box

pallet = Pallet()
pallet.choose_pallet_type()
index = int(input("Choose pallet type:\n")) - 1
pallet.set_pallet_type(index)

if index == 0:
    pallet.euro_pallet()
elif index == 1:
    pallet.blok_pallet()

box = Box()
box.choose_box()
index_box = int(input("Choose box type:\n")) -1

if index_box == 0:
    box.box_type_a()


def boxes_per_layer():
    # only correct in case of euro pallet
    boxes_on_length = pallet.pallet_length/box.box_length
    boxes_on_width = pallet.pallet_width/box.box_width
    return boxes_on_length * boxes_on_width


print(40 * "-")
print("Pallet type:", pallet.pallet_type)
print("Pallet length", pallet.pallet_length, "cm")
print("Pallet width:", pallet.pallet_width, "cm")
print(40 * "-")
print("Box dimensions (L x W x H):", box.box_length,"x", box.box_width, "x", box.box_height, "cm")
print(40 * "-")
print("boxes per layer:", boxes_per_layer())