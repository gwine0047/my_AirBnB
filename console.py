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

class HBNBCommand(cmd.Cmd):
    """
    command interpreter
    """
    prompt = "(godwin) "
    valid_classes = ["BaseModel", "User", "Godwin"]

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




# to make sure the file does not run  when imported do:
if __name__ == "__main__":
    HBNBCommand().cmdloop()