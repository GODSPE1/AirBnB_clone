#!/usr/bin/python3
"""This module defines the  console"""
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """This is all about the functions in the HBNB command"""

    prompt = "(hbnb) "


    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """

        if line:
            if line == "BaseModel":
                base = BaseModel()
                base.save()
                print(base.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234.
        """
        from models.__init__ import storage
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            class_name, instance_id = args
            objects = storage.all()
            instance_key = "{}.{}".format(class_name, instance_id)
            if instance_key in objects:
                print(objects[instance_key])
            else:
                print("** no instance found **")



    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id.
        """
        from models.__init__ import storage
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            class_name, instance_id = args
            objects = storage.all()
            if class_name.lower() not in storage.classes():
                print("** class doesn't exist **")
            else:
                instance_key = "{}.{}".format(class_name, instance_id)
                if instance_key in objects:
                    del objects[instance_key]
                    storage.save()
                    if not any(instance.startswith(class_name + '.') for instance in objects.keys()):
                        del storage.classes()[class_name.lower()]
                else:
                    print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Ex: $ all BaseModel or $ all.
        """
        from models.__init__ import storage
        if line:
            try:
                classs = eval(line.split()[0])
            except NameError:
                print("** class doesn't exist **")
                return
                print([str(obj) for obj in storage.all().values() if isinstance(obj, cls)])
        else:
            print([str(obj) for obj in storage.all().values()])


    def do_update(self, line):
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** value missing **")
        elif len(args) == 3:
            class_name, attribut_name, attribut_value = args


    def do_EOF(self, line):
        """Handles end of the file to exit the program"""
        exit(0)
    
    def emptyline(self):
        """Overides the cmd emptyline"""
   
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
    def default(self, line):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
