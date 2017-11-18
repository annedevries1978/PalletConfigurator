class Pallet(object):
    def __init__(self):
        self.pallet_type_list = ["Euro pallet", "Blok pallet"]
        self.pallet_type = ""
        self.pallet_length = ""
        self.pallet_width = ""

    def euro_pallet(self):
        self.pallet_length = 120
        self.pallet_width = 80

    def blok_pallet(self):
        self.pallet_length = 120
        self.pallet_width = 100

    def choose_pallet_type(self):
        choice = 0
        for self.pallet_type in self.pallet_type_list:
            choice += 1
            print(str(choice) + ":", self.pallet_type)

    def set_pallet_type(self, index):
        self.pallet_type = self.pallet_type_list[index]

    def get_pallet_type(self):
        return self.pallet_type, \
               self.pallet_width, \
               self.pallet_length

class Box(object):
    def __init__(self):
        self.type_list = ['A', 'B', 'C']
        self.type = ""
        self.box_length = ""
        self.box_width = ""
        self.box_height = ""

    def choose_box(self):
        choice = 0
        for self.type in self.type_list
