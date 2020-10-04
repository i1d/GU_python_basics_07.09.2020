"""5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
"""

###################################################################################################
#код ниже - почти без валидаторов - при передаче параметров за пределами разумного будет крашиться#
#код с валидаторами - в task_6.py                                                                 #
###################################################################################################


import task_4
from datetime import datetime
from sys import exit

f_out = "task_4_out.txt"
with open(f_out, "w", encoding='UTF-8') as f_out:
    f_out.write("Logging passing warehouse items to departments.\n")


def log(data):
    f_out = "task_4_out.txt"
    with open(f_out, "a+", encoding='UTF-8') as f_out:
        f_out.write(data + "\n")


class WarehouseError(Exception):
    def __init__(self, text):
        self.text = text


class UI:
    @staticmethod
    def warehouse_action():
        ask_user = "0 - create a warehouse\n" \
                   "1 - check the warehouse status\n" \
                   "2 - put an item to the warehouse\n" \
                   "3 - remove an item from the warehouse and send it somewhere\n" \
                   "4 - empty warehouse by destroying all items\n" \
                   "5 - quit\n" \
                   "> "
        while True:
            try:
                user_action = int(input(ask_user))
                if user_action not in (0, 1, 2, 3, 4, 5):
                    raise WarehouseError("Wrong choice, please choose correct option:")
            #        return user_answer
            except ValueError:
                print('Wrong input. Try again.')
                continue
            except WarehouseError as err:
                print(err)
                continue
            else:
                return user_action

    @staticmethod
    def equipment_choice():
        ask_user = "1 - printer\n" \
                   "2 - scanner\n" \
                   "3 - xerox\n" \
                   "5 - back to main menu\n" \
                   "> "
        while True:
            try:
                user_action = int(input(ask_user))
                if user_action not in (1, 2, 3, 5):
                    raise WarehouseError("Wrong choice, please choose correct option:")
            #        return user_answer
            except ValueError:
                print('Wrong input. Try again.')
                continue
            except WarehouseError as err:
                print(err)
                continue
            else:
                return user_action

class Warehouse(task_4.Warehouse):
    def __init__(self, capacity):
        super().__init__(capacity)

    def put_obj(self, obj):
        print(f'...Trying to load "{obj.unit_name}" to the warehouse...')
        self.objects.append(obj)
        #   print(f'im put_obj method. obj.unit_size={obj.unit_size}')
        self.space_occupied += obj.unit_size
        #   print(f'self occupied = {self.space_occupied}')
        print(f'..."{obj.unit_name}" loaded successfully!')

    def __getitem__(self, idx):
        return self.objects[idx]

    def pass_obj(self, obj, dept):
        print(f'...Trying to pass "{obj.unit_name}" from the warehouse to "{dept}" department...')
        self.objects.remove(obj)
        self.space_occupied -= obj.unit_size
        # логируем в файл о переданном оборудовании
        log(f'{datetime.now()}. An object "{obj.unit_name}" has been moved to "{dept}" department.')
        print(f'..."{obj.unit_name}" removed successfully!')

#    @staticmethod


 #   @classmethod
 #   def create_warehouse(cls, capacity):
 #       return cls(Warehouse(capacity))

  #  @classmethod
 #   def check_warehouse(self):
 #       print(f'Current warehouse condition: {vars(self)}')


if __name__ == '_main__':  # make some tests here to check the objects
    printer1 = task_4.Printer("a_printer", 10000.13, 2, 53.1, 100)
    printer2 = task_4.Printer("a_2_printer", 200000, 10, 150, 200)
    scanner1 = task_4.Scanner("a_scanner", 29999.99, 3, 89.9, 1200)
    xerox1 = task_4.Xerox("a_xerox", 80000, 4, 125, 300, 1200, True)
    #   print(vars(printer1))
    #   print(vars(printer2))
    #   print(vars(scanner1))
    #   print(vars(xerox1))

    warehouse = Warehouse(100)
    print(f'Empty warehouse: {vars(warehouse)}')

    warehouse.put_obj(printer1)
    warehouse.put_obj(scanner1)
    warehouse.put_obj(xerox1)
    warehouse.put_obj(printer2)

    print(f'Current warehouse condition: {vars(warehouse)}')

    print(f'try to get an obj 1: {vars(warehouse[1])}')
    print(f'Current warehouse condition: {vars(warehouse)}')
    print("=" * 20)
    print(f'warehouse objects: {warehouse.objects}.\ntype: {type(warehouse.objects)}')
    print(f'removing of {printer2}...')
    warehouse.pass_obj(printer2, "IT")
    warehouse.pass_obj(printer1, "ADM")
    print(f'Current warehouse condition: {vars(warehouse)}')


def equipment_choice():
    while True:
        action = UI.equipment_choice()

        if action == 1:
            # task_4.Printer("a_printer", 10000.13, 2, 53.1, 100)
            name = input("Enter printer name: ")
            price = float(input("Enter printer price: "))
            size = int(input("Enter printer size: "))
            weight = float(input("Enter printer weight: "))
            ppm = int(input("Enter printer PPM: "))
            eq = task_4.Printer(name, price, size, weight, ppm)
        elif action == 2:
            #scanner1 = task_4.Scanner("a_scanner", 29999.99, 3, 89.9, 1200)
            name = input("Enter scanner name: ")
            price = float(input("Enter scanner price: "))
            size = int(input("Enter scanner size: "))
            weight = float(input("Enter scanner weight: "))
            dpi = int(input("Enter scanner DPI: "))
            eq = task_4.Scanner(name, price, size, weight, dpi)
        elif action == 3:
            #task_4.Xerox("a_xerox", 80000, 4, 125, 300, 1200, True)
            name = input("Enter xerox name: ")
            price = float(input("Enter xerox price: "))
            size = int(input("Enter xerox size: "))
            weight = float(input("Enter xerox weight: "))
            ppm = int(input("Enter xerox PPM: "))
            dpi = int(input("Enter xerox DPI: "))
            b = "n"
            while True:
                try:
                    b = input("Have brochure-maker? (y/n): ").lower()
                    if b not in ("y", "n"):
                        raise WarehouseError("Please choose y or n.")
                except WarehouseError as err:
                    print(err)
                    continue
                else:
                    break
            if b == "n":
                brochure = False
            elif b == "y":
                brochure = True
            eq = task_4.Xerox(name, price, size, weight, ppm, dpi, brochure)
        elif action == 5:
            break
        return eq


#def object_choice():
#    for obj, num in enumerate(warehouse.objects, 1):
#        print(f'{num}:{obj}')
#    i = int(input("choose object number: "))
#    obj = warehouse.objects(i - 1)
#    return obj


def action():
    while True:
        action = UI.warehouse_action()

        if action == 0:
            try:
                wh_size = int(input("Enter warehouse size to create: "))
                warehouse = Warehouse(wh_size)
                print("Warehouse created!")
            except ValueError as err:
                print(f"Warehouse capacity size must be integer. Details: {err}.")
        elif action == 1:
            obj_list = [obj.unit_name for obj in warehouse.objects]
            print(f'Current warehouse: Capacity={warehouse.capacity}, Objects={obj_list}, Occupied space={warehouse.space_occupied}.')
            if warehouse.space_occupied == 0:
                print(f"Seems warehouse is empty, let's put something in!")
        elif action == 2:
            print("Let's create an item and put it to the Warehouse!")
            warehouse.put_obj(equipment_choice())
        elif action == 3:
            print("There are next items on the warehouse: ")
            obj_list = [vars(obj) for obj in warehouse.objects]
            for num, obj in enumerate(obj_list, 1):
                print(f'#{num} : {obj}')
            i = int(input("Choose object number to remove and dispatch: "))
            obj = warehouse.objects[i - 1]
            dept = input("Enter department name to dispatch equipment from the warehouse: ")
            warehouse.pass_obj(obj, dept)
            #  remove_warehouse()
        elif action == 4:
            print("...Clearing warehouse...")
            print("...Destroying items...")
            warehouse.objects.clear()
            warehouse.space_occupied = 0
            print("...Done!")
        elif action == 5:
            print("Thanks for visiting. Bye.")
            exit()


if __name__ == '__main__':
    print("\nWelcome to the Warehouse! What would you like to do today?")
  #  a = Warehouse.action()
    action()



