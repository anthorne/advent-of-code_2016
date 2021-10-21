# Day 10

# --- Variables ---
holders = []
chips = []
value_instructions = []


# --- Classes ---
class Holder:
    def __init__(self, name):
        self.name = str(name)
        self.items = []
        self.instructions = []

    def add_item(self, item):
        self.items.append(item)
        self.check_items()

    def add_instruction(self, instruction):     # Each instruction having ['low_to', 'high_to'] string names
        self.instructions.append(instruction)

    def exec_instruction(self):
        instruction = self.instructions.pop()
        if len(self.items) == 2:
            chip_low = ''
            chip_high = ''
            chip_value = -1
            for item in self.items:
                if chip_low == '':
                    chip_low = item
                    chip_value = item.value
                else:
                    if item.value > chip_value:
                        chip_high = item
                    else:
                        chip_high = chip_low
                        chip_low = item
            self.items.clear()
            if check_goal_part_one(chip_low, chip_high):
                print('\n - Part one - The holder: ' + self.name + ' is responsible for comparing chips ' + str(chip_low.value) + ' and ' + str(chip_high.value))
            give_chip(chip_low, instruction[0])
            give_chip(chip_high, instruction[1])
        else:
            print('Error: ' + self.name + ' does not have two chips!')

    def check_items(self):
        num_items = len(self.items)
        num_instructions = len(self.instructions)
        if num_items >= 2:
            if num_instructions >= 1:
                self.exec_instruction()
                return True
            else:
                print('Error: ' + self.name + ' has ' + str(num_items) + ' items but no instructions!')
                return False
        else:
            return False


class Chip:
    def __init__(self, value):
        self.value = value


# --- Functions ---
# Read file input instructions and execute
def read_instructions():
    file_obj = open('d10_input.txt', 'r')
    for line in file_obj:
        if line != '\n':
            if line.split(' ')[0] == 'bot':       # ex. "bot 201 gives low to bot 162 and high to bot 83"
                bot = line.split(' ')[0] + ' ' + line.split(' ')[1].strip('\n')
                low_to = line.split(' ')[5] + ' ' + line.split(' ')[6].strip('\n')
                high_to = line.split(' ')[10] + ' ' + line.split(' ')[11].strip('\n')
                giver_obj = get_holder_obj(bot)
                giver_obj.add_instruction([low_to, high_to])

            elif line.split(' ')[0] == 'value':                               # ex. "value 41 goes to bot 190"
                bot = line.split(' ')[4] + ' ' + line.split(' ')[5].strip('\n')
                chip = line.split(' ')[1].strip('\n')
                value_instructions.append([chip, bot])

            else:
                print('Error: Cannot interpret command, ' + line)


# Execute the value command to give a chip to a holder
def exec_value():
    for instruction in value_instructions:
        chip_obj = get_chip_obj(instruction[0])
        holder_obj = get_holder_obj(instruction[1])
        if not check_chip_owner(chip_obj):
            holder_obj.add_item(chip_obj)
        else:
            chip_owner = check_chip_owner(chip_obj)
            print('Error: The chip: ' + str(instruction[0]) + ' has a holder: ' + str(chip_owner.name))


# Give a chip object to a holder based on holder's name
def give_chip(chip_obj, holder_name):
    holder_obj = get_holder_obj(holder_name)
    holder_obj.add_item(chip_obj)


# Get or create chip object
def get_chip_obj(chip_value):
    for chip in chips:
        if chip.value == chip_value:
            return chip
    new_chip = Chip(chip_value)
    chips.append(new_chip)
    return new_chip


# Get or create holder object
def get_holder_obj(name):
    for holder in holders:
        if holder.name == name:
            return holder
    new_holder = Holder(name)
    holders.append(new_holder)
    return new_holder


# Checks if a chip has an owner and returns the owner object, if the chip has no owner the function returns False
def check_chip_owner(chip_obj):
    for holder in holders:
        for item in holder.items:
            if item == chip_obj:
                return holder
    return False


# Checks if the goal for part one is achieved
def check_goal_part_one(low, high):
    goal = ['17', '61']
    if [low.value, high.value] == goal:
        return True
    else:
        return False


def list_objects():
    for holder in holders:
        print('Holder: ' + holder.name + ' has items: ' + str(holder.items) + ' and instructions: ' + str(holder.instructions))
    for chip in chips:
        print('Chip: ' + str(chip.value))


# main

read_instructions()
exec_value()
# list_objects()

# Part one - answer : 53 is too low!,       199 is too high     -- right answer : 113


a = get_holder_obj('output 0')
b = get_holder_obj('output 1')
c = get_holder_obj('output 2')

result = 1
for i in a.items:
    result *= int(i.value)
for j in b.items:
    result *= int(j.value)
for k in c.items:
    result *= int(k.value)

print(' - Part two - Multiply chip values in outputs 0, 1, and 2 = ' + str(result))

# Part two - answer : 47519 is too high!                        -- right answer : 12803
