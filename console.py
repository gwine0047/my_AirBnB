#!/usr/bin/python3

"""
 contains the entry point of the command interprete
"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.godwin import Godwin
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class HBNBCommand(cmd.Cmd):
    """
    command interpreter
    """
    prompt = "(godwin) "
    valid_classes = ["BaseModel", "User", "Godwin", "Amenity", "Place", "Review", "State", "City"]

    def do_quit(self, arg):
        """
        to exit the program
        """
        return True
    
    def emptyline(self):
        """
        does nothing when an emptyline command
        is entered.
        """
        pass

    def help_quit(self, arg):
        """
        help command for quit command
        """
        print("Quit command to exit the program")
        return True

    def do_EOF(self, arg):
        """
        handles EOF command
        """
        print()
        return True

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and 
        prints the id
        """
        # use shlex to split arguments and saves to a list (commands)
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f'{commands[0]}()')
            storage.save()
            print(f"Your new object has been created and the id = {new_instance.id}")

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
         """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            # if both class and id are provided, fetch all objects from storage and check if id is present
            objects = storage.all()

            # make a key with the provided arguments
            key = f"{commands[0]}.{commands[1]}"

            if key in objects:
                print(f'The searched object is found and is printed below:\n{objects[key]}')
            else:
                print("** no instance found **")


    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id 
        (save the change into the JSON file)
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print('** class name missing **')
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = f'{commands[0]}.{commands[1]}'
            if key in objects:
                print(f'The object with id: {commands[1]} has been deleted')
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all 
        instances based or not on the class name
        """
        objects = storage.all()

        commands = shlex.split(arg)
        print(f'your commands = {commands}')
        if len(commands) == 0:
            # no specific class was passed, so all classes are printed
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                # Let's extract the class name from the key before comparism
                if key.split('.')[0] == commands[0]:
                    print(str(value))

    def do_update(self, arg):
        """
        Updates an instance based on the class name 
        and id by adding or updating attribute 
        (save the change into the JSON file)
        """

        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = f'{commands[0]}.{commands[1]}'
            if key not in objects:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("** value missing **")
            else:
                obj_to_update = objects[key]
                attr_name = commands[2]
                attr_value = commands[3]

                try:
                    # the value is received as a string. eval helps to convert to the right
                    # datatype(e.g int(value), str(value), bool(value))
                    attr_value = eval(attr_value)
                except Exception:
                    pass
                setattr(obj_to_update, attr_name, attr_value)
                obj_to_update.save()
    
    def default(self, arg):
        """
        handles default behaviour for invalid syntaxes
        """
        arg_list = arg.split('.')
        # User.all() = ['User', 'all()']
        # print(f"arg_list = {arg_list}")

        incoming_classname = arg_list[0]
        # print(f"incoming method class name = {incoming_classname}")

        # splitting tha method all()
        command = arg_list[1].split('(')
        # command[0] = all and command[1] = )
        
        incoming_method = command[0]
        # print(f"incoming method = {incoming_method}")

        method_dict = {
            'all': self.do_all,
            'show' : self.do_show,
            'destroy' : self.do_destroy,
            'update' : self.do_update,
            'count' : self.do_count
        }
        if incoming_method in method_dict.keys():
            # return something like 'all User' mimicking a method call
            # self.all(self, User)
            return method_dict[incoming_method]("{} {}".format(incoming_classname, ''))
        print("** unknown syntax: {}".format(arg))
        return False

    def do_count(self, arg):
        """
        retrieve the number of instances of a class
        <class name>.count()
        """
        objects = storage.all()

        commands = shlex.split(arg)

        if arg:
            class_name = commands[0]
        else:
            print("** class name missing **")
        count = 0

        if commands:
            if class_name in self.valid_classes:
                for obj in objects.values():
                    if obj.__class__.__name__ == class_name:
                        count += 1
                print(count)
            else:
                print("** not **")
        else:
            print("** classname doesn't exist **")



# to make sure the file does not run  when imported do:
if __name__ == "__main__":
    HBNBCommand().cmdloop()