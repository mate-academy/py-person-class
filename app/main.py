from typing import List, Dict, Optional, Union  # we use "Optional" to indicate that the return data can be None


class Person:
    people: Dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife: Optional["Person"] = None
        self.husband: Optional["Person"] = None
        self.__class__.people[name] = self  # Add an instance of the class to the people dictionary by the key "name"

    def __repr__(self) -> str:
        return f"Person({self.name}, {self.age})"


def create_person_list(people_list: List[Dict[str, Union[str, int, None]]]) -> List[Person]:
    person_instances: List[Person] = []

    for person_data in people_list:
        name: str = person_data['name']
        age: int = person_data['age']
        person_instance = Person(name, age)  # Create an instance of the Person class
        person_instances.append(person_instance)  # Add an instance of the class to the person_instances list

    for person_data in people_list:
        name: str = person_data['name']
        person_instance = Person.people[name]  # Get a class instance by name from the dictionary people

        if 'wife' in person_data and person_data['wife'] is not None:
            wife_name: str = person_data['wife']
            person_instance.wife = Person.people[wife_name]  # Set the wife attribute

        if 'husband' in person_data and person_data['husband'] is not None:
            husband_name: str = person_data['husband']
            person_instance.husband = Person.people[husband_name]  # Set the husband attribute

    return person_instances  # Return a list of instances of the Person class
