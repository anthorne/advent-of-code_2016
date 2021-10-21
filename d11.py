# TODO: Solution is not ready!
import sys, time, keyboard


# Input
#
# The first floor contains
#       a polonium generator,               POG
#       a thulium generator,                THG
#       a thulium-compatible microchip,     THM
#       a promethium generator,             PRG
#       a ruthenium generator,              RUG
#       a ruthenium-compatible microchip,   RUM
#       a cobalt generator,                 COG
#   and a cobalt-compatible microchip.      COM
#
# The second floor contains
#       a polonium-compatible microchip     POM
#   and a promethium-compatible microchip.  PRM
#
# The third floor contains nothing relevant.
# The fourth floor contains nothing relevant.

#         F   E    POG    POM    THG    THM    PRG    PRM    RUG    RUM    COG    COM

floors = [4, '.', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . '], \
         [3, '.', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . '], \
         [2, '.', ' . ', 'POM', ' . ', ' . ', ' . ', 'PRM', ' . ', ' . ', ' . ', ' . '], \
         [1, 'E', 'POG', ' . ', 'THG', 'THM', 'PRG', ' . ', 'RUG', 'RUM', 'COG', 'COM']


class Game:
    def __init__(self):
        self.win = False
        self.pointer = 99
        self.selected = []
        self.update_pointer()

    def update_pointer(self):
        f = get_floor_items()
        self.pointer = 99
        for i in f:
            for c in i:
                if type(c) == int:
                    if self.pointer > c:
                        self.pointer = c

    def num_selected(self):
        return len(self.selected)


class Elevator:
    def __init__(self):
        self.items = []             # [item, item_position]
        self.current_floor = 1
        self.num_moves = 0

    def add(self, thing):
        # Check if input object already is in items list
        for i in self.items:
            if i[0] == thing:
                return False

        # The capacity rating means it can carry at most yourself and two RTGs or microchips in any combination.
        if len(self.items) > 1:
            # print('Error: Elevator full! - count: ' + str(len(self.items)) + ' - items: ' + str(self.items))
            return False

        # Check the input object if it exists on the elevator floor
        thing_position = 0
        thing_exist = False
        for f in floors:
            if f[1] == 'E':
                counter = -2
                for c in f:
                    if c == thing:
                        thing_exist = True
                        thing_position = counter
                    counter += 1
        if not thing_exist:
            print('Problem locating the object: ' + str(thing) + '! Floor-dump: ' + str(floors))
            return False
        self.items.append([thing, thing_position])

    def move(self, direction):
        # The elevator will only function if it contains at least one RTG or microchip.
        if len(self.items) == 0:
            print_there(17, 4, 'Error: The elevator will only function if it contains at least one RTG or microchip.')
            return False
        # Check direction input
        if direction != 'u' and direction != 'd':
            print('Error moving the elevator: ' + str(direction))
            return False
        # Check if move is valid
        new_floor = 0
        if direction == 'd':
            if self.current_floor <= 1:
                # print('Cannot move elevator down from floor: ' + str(self.current_floor))
                return False
            new_floor = self.current_floor - 1
        elif direction == 'u':
            if self.current_floor >= 4:
                # print('Cannot move elevator up from floor: ' + str(self.current_floor))
                return False
            new_floor = self.current_floor + 1

        # The elevator always stops on each floor to recharge, and this takes long enough that the
        #                       items within it and the items on that floor can irradiate each other.
        # Test move the elevator to see if it fries any microchip
        test_floor = []
        for floor in floors:
            if floor[0] == new_floor:
                for f in floor:
                    test_floor.append(f)
                test_floor[1] = 'E'
                for i in self.items:
                    test_floor[i[1]] = str(i[0])
        if chips_fried(test_floor):
            print_there(17, 4, 'Error: This move will fry the microchips! Floor dump: ' + str(test_floor))
            return False

        # Perform the move
        for floor in floors:
            if floor[0] == new_floor:
                floor[1] = 'E'
                for i in self.items:
                    floor[(i[1] + 2)] = str(i[0])
            elif floor[0] == self.current_floor:
                floor[1] = '.'
                for i in self.items:
                    floor[(i[1] + 2)] = ' . '
        self.items = []
        self.num_moves += 1
        self.current_floor = new_floor

    def num_items(self):
        return len(self.items)

    def print_info(self):
        print_there(13, 4, ' Elevator items: ' + str(self.items) +
                           ' - Number of moves: ' + str(self.num_moves) +
                           ' - Current floor: ' + str(self.current_floor))


# Checks if chips are fried at a floor
def chips_fried(floor):
    # If a chip is ever left in the same area as another RTG,
    # and it's not connected to its own RTG, the chip will be fried.

    # Check if no RTG is found, then we're safe
    rtgs_found = []
    for c in floor:
        if str(c)[-1:] == 'G':
            rtgs_found.append(c)
    if len(rtgs_found) == 0:
        return False

    # print('\n\n\n\n\ngenerators found: ' + str(rtgs_found))

    # Check if microchips is found
    chips_found = []
    for c in floor:
        if str(c)[-1:] == 'M':
            chips_found.append(c)

    # print('microchips found: ' + str(chips_found))

    # Remove chips from list if they are connected to their generator
    chips_to_be_removed = []
    for c in chips_found:
        for g in rtgs_found:
            if c[0:2] + 'G' == g:
                chips_to_be_removed.append(c)
    for c in chips_to_be_removed:
        chips_found.remove(c)

    # print('microchips after remove: ' + str(chips_found))

    # Check if chips found is exposed to other generators
    for c in chips_found:
        for g in rtgs_found:
            if c[0:2] + 'G' != g:
                # print('chip: ' + str(c) + ' is exposed to other generator: ' + str(g) + ' and gets fried!! BZZzzhrrgghhz..')
                return True

    return False


# Prints out the floors
def print_floors():
    counter = 3
    for floor in floors:
        counter += 1
        row = ' F'
        for col in floor:
            row += str(col) + '  '
        print_there(counter, 4, row)


# Print text on specific position - Linux only
def print_there(x, y, text):
    # sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
    # sys.stdout.flush()
    space = ""
    for i in range(y):
        space += " "
    print(str(space) + str(text))


def get_floor_items():
    items = []
    for f in floors:
        if f[1] == 'E':
            counter = -2
            for c in f:
                if c != ' . ' and counter >= 0:
                    items.append([counter, c])
                counter += 1
    return items


def get_input():
    # print selectable items
    floor_items = get_floor_items()
    item_low_pos = 99
    item_high_pos = -1
    print_there(9, 4, ' ' * 80)
    for i in floor_items:
        for c in i:
            if type(c) == int:
                if item_low_pos > c:
                    item_low_pos = c
                if item_high_pos < c:
                    item_high_pos = c
                pos = 12
                offset = 5 * c
                pos += offset
                print_there(9, pos, '[ ]')

    # print selected items
    for i in g.selected:
        pos = 13
        offset = 5 * i
        pos += offset
        print_there(9, pos, 'X')

    # print pointer
    print_there(10, 4, ' ' * 80)
    pos = 13
    offset = 5 * g.pointer
    pos += offset
    print_there(10, pos, '|')

    # get input
    key = keyboard.read_key(True)
    time.sleep(0.5)
    to_elevator = ''
    print_there(11, 4, ' ' * 80)
    print_there(13, 4, ' ' * 80)
    print_there(16, 4, ' ' * 80)
    print_there(17, 4, ' ' * 80)

    # a or key_left = to the left
    if key == 'a' or key == 'D':
        if g.pointer > item_low_pos:
            previous_item = g.pointer
            for i in floor_items:
                for c in i:
                    if type(c) == int:
                        if int(c) == int(g.pointer):
                            g.pointer = previous_item
                        previous_item = c
        print_there(11, 4, 'Going left..')

    # d or key_right = to the right
    elif key == 'd' or key == 'C':
        if g.pointer < item_high_pos:
            next_item = False
            for i in floor_items:
                for c in i:
                    if type(c) == int:
                        if next_item:
                            g.pointer = int(c)
                            next_item = False
                            break
                        if int(c) == int(g.pointer):
                            next_item = True
        print_there(11, 4, 'Going right..')

    # space = select to be added to elevator
    elif key == 'space':
        # check if already selected, in that case un-select it
        found = False
        for i in g.selected:
            if i == g.pointer:
                found = True
                g.selected.remove(g.pointer)
                print_there(11, 4, 'Removing item: ' + str(g.pointer))
        if not found:
            # check if items list is full
            # print(' num selected items; ' + str(g.num_selected()))
            if g.num_selected() == 2:
                print_there(11, 4, 'You have already selected two items')
                return False
            g.selected.append(g.pointer)
            print_there(11, 4, 'Adding item: ' + str(g.pointer))

    # w or key_up = take the elevator up
    elif key == 'w' or key == 'A':
        print_there(11, 4, 'Going up the elevator with items: ' + str(g.selected))
        to_elevator = 'u'

    # s or key_down = take the elevator down
    elif key == 's' or key == 'B':
        print_there(11, 4, 'Going down the elevator with items: ' + str(g.selected))
        to_elevator = 'd'

    # q = quit
    elif key == 'q':
        quit()

    # Handle the elevator
    if to_elevator == 'u' or to_elevator == 'd':
        add_ok = False
        # print('\n -- g.selected: ' + str(g.selected) + ' -- floor_items: ' + str(floor_items))
        for i in g.selected:
            for f in floor_items:
                if f[0] == i:
                    add_ok = e.add(f[1])
        if not e.move(to_elevator):
            g.selected = []
        g.update_pointer()


def check_win():
    for f in floors:
        if f == [4, 'E', 'POG', 'POM', 'THG', 'THM', 'PRG', 'PRM', 'RUG', 'RUM', 'COG', 'COM']:
            print_floors()
            e.print_info()
            g.win = True


# Create the elevator object
e = Elevator()
g = Game()

print('\n\n\n\n\n\n\n\n\n\n\n\n')

while not g.win:
    print_floors()
    get_input()
    check_win()
    e.print_info()

