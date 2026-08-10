import ast
import os

def path_to_main():
    base_path = os.path.join("app", "main.py")
    return (
        base_path if os.path.exists(base_path) else os.path.join(os.pardir, base_path)
    )



def person_instance_attribute_wife_and_husband_doesnt_exists():
    with open(path_to_main()) as file:
        tree = ast.parse(file.read())

    print(tree.__dict__["body"][0]
            .__dict__["body"][1]
            .__dict__["args"]
            .__dict__["args"])
person_instance_attribute_wife_and_husband_doesnt_exists()

