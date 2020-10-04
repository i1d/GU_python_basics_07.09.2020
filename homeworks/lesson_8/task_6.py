"""6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""

###########################################
#ниже- task_5.py + дополнения + валидаторы#
###########################################


import task_4
from datetime import datetime
from sys import exit

f_out = "task_6_out.txt"
with open(f_out, "w", encoding='UTF-8') as f_out:
    f_out.write("Logging passing warehouse items to departments.\n")


def log(data):
    f_log = "task_6_out.txt"
    with open(f_log, "a+", encoding='UTF-8') as f_log:
        f_log.write(data + "\n")


class WarehouseError(Exception):
    def __init__(self, text):
        self.text = text


def num_inp_check(f, st, limit):
    while True:
        try:
            num = f(input(st))
            if num < limit:
                raise WarehouseError(f"This value is < {limit}. Try again. ")
        except WarehouseError as err:
            print(err)
            continue
        except ValueError as err:
            print(f'This value is wrong. Try again. Details: {err}')
            continue
        else:
            return num
            break


def str_inp_check(st, limit):
    while True:
        try:
            s = input(st)
            if len(s) == 0:
                raise WarehouseError(f'This name cannot be empty. Try again.')
            elif len(s) <= limit:
                raise WarehouseError(f'This name is too short (<={limit}). Try again.')
        except WarehouseError as err:
            print(err)
            continue
        else:
            return s
            break


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
                    raise WarehouseError("Wrong choice, please choose correct option: ")
            except ValueError as err:
                print(f'Wrong input. Try again. Details: {err}')
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
                    raise WarehouseError("Wrong choice, please choose correct option: ")
            except ValueError as err:
                print(f'Wrong input. Try again. Details: {err}')
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
        while True:
            try:
                if self.space_occupied + obj.unit_size > self.capacity:
                    raise WarehouseError(f"Oops! There are not enough space in the Warehouse!\n"
                                         f"   Current warehouse capacity={self.capacity};\n"
                                         f"   Current occupied space={self.space_occupied};\n"
                                         f"   But you tried to load an item with size={obj.unit_size}!")
            except WarehouseError as err:
                print(err)
                break
            else:
                self.objects.append(obj)
                self.space_occupied += obj.unit_size
                print(f'..."{obj.unit_name}" loaded successfully!')
                break

    def pass_obj(self, obj, dept):
        print(f'...Trying to pass "{obj.unit_name}" from the warehouse to "{dept}" department...')
        self.objects.remove(obj)
        self.space_occupied -= obj.unit_size
        # логируем в файл информацию о переданном оборудовании
        log(f'{datetime.now()}. An object "{obj.unit_name}" has been moved to "{dept}" department.')
        print(f'..."{obj.unit_name}" removed successfully!')


def equipment_choice():
    while True:
        act = UI.equipment_choice()
        if act == 1:  # выбираем принтер
            name = str_inp_check("Enter printer name: ", 3)
            price = num_inp_check(float, "Enter printer price: ", 0)
            size = num_inp_check(int, "Enter printer size: ", 1)
            weight = num_inp_check(float, "Enter printer weight: ", 1)
            ppm = num_inp_check(int, "Enter printer PPM: ", 1)
            return task_4.Printer(name, price, size, weight, ppm)
        elif act == 2:  # выбираем сканер
            name = str_inp_check("Enter scanner name: ", 3)
            price = num_inp_check(float, "Enter scanner price: ", 0)
            size = num_inp_check(int, "Enter scanner size: ", 1)
            weight = num_inp_check(float, "Enter scanner weight: ", 1)
            dpi = num_inp_check(int, "Enter scanner DPI: ", 1)
            return task_4.Scanner(name, price, size, weight, dpi)
        elif act == 3:  # выбираем ксерокс
            name = str_inp_check("Enter xerox name: ", 3)
            price = num_inp_check(float, "Enter xerox price: ", 0)
            size = num_inp_check(int, "Enter xerox size: ", 1)
            weight = num_inp_check(float, "Enter xerox weight: ", 1)
            ppm = num_inp_check(int, "Enter xerox PPM: ", 1)
            dpi = num_inp_check(int, "Enter xerox DPI: ", 1)
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
            return task_4.Xerox(name, price, size, weight, ppm, dpi, brochure)
        elif act == 5:
            break


def action():
    while True:
        try:
            action = UI.warehouse_action()
            if action == 0:
                while True:
                    print("Trying to create a warehouse...")
                    try:
                        wh_size = int(input("Enter warehouse size to create: "))
                        if wh_size <= 0:
                            raise WarehouseError("Warehouse size must be > 0. Try again.")
                    except WarehouseError as err:
                        print(err)
                    except ValueError as err:
                        print(f"Warehouse capacity size must be integer. Details: {err}.")
                    else:
                        warehouse = Warehouse(wh_size)
                        print("Warehouse created!")
                        break
            elif action == 1:
                try:
                    obj_list = [obj.unit_name for obj in warehouse.objects]
                    print(f'Current warehouse state:\n'
                          f'   Capacity={warehouse.capacity}\n'
                          f'   Occupied space={warehouse.space_occupied}\n'
                          f'   Objects={obj_list}')
                    if warehouse.space_occupied == 0:
                        print(f"The warehouse is empty, let's put something in!")
                    elif warehouse.space_occupied == warehouse.capacity:
                        print(f"The warehouse is full! Dispatch some item or even destroy anything!")
                except UnboundLocalError:
                    print("Seems there are no warehouse yet. Let's go and create one!")
            elif action == 2:
                try:
                    print("Let's create an item and put it to the Warehouse!")
                    warehouse.put_obj(equipment_choice())
                except UnboundLocalError:
                    print("Seems there are no warehouse yet. Let's go and create one!")
                except AttributeError:
                    continue
            elif action == 3:
                try:
                    if len(warehouse.objects) > 0:
                        print("There are next items on the warehouse: ")
                        obj_list = [vars(obj) for obj in warehouse.objects]
                        obj_nums = []
                        for num, obj in enumerate(obj_list, 1):
                            print(f'#{num} : {obj}')
                            obj_nums.append(num)
                        while True:
                            try:
                                i = int(input("Choose object number to remove and dispatch: "))
                                if i not in obj_nums:
                                    raise WarehouseError("Such object does not exist, try again.")
                            except WarehouseError as err:
                                print(err)
                                continue
                            except ValueError:
                                print("Not a number, try again.")
                                continue
                            else:
                                obj = warehouse.objects[i - 1]
                                break
                        dept = input("Enter department name to dispatch equipment from the warehouse: ")
                        warehouse.pass_obj(obj, dept)
                    else:
                        print("This warehouse is empty!")
                except UnboundLocalError:
                    print("Seems there are no warehouse yet. Let's go and create one!")
            elif action == 4:
                try:
                    if warehouse.space_occupied > 0:
                        print("...Clearing warehouse...")
                        print("...Destroying items...")
                        warehouse.objects.clear()
                        warehouse.space_occupied = 0
                        print("...Done!")
                    else:
                        print("This warehouse is already empty, nothing to clear and destroy.")
                except UnboundLocalError:
                    print("Seems there are no warehouse yet. Let's go and create one!")
            elif action == 5:
                print("Thanks for visiting the Warehouse Inc! Bye.")
                exit()
        except KeyboardInterrupt:
            print("Sorry to hear that you would like to quit. Hope to see you another time in the Warehouse Inc! Bye.")
            exit()


if __name__ == '__main__':
    print("Welcome to the Warehouse Inc! What would you like to do today?\n")
    action()
