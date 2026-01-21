class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    # Create all Person instances without setting wife/husband attributes yet
    person_objects = [
        Person(person["name"], person["age"]) for person in people_list
    ]

    # Set wife/husband attributes for relevant Person instances
    for person_dict in people_list:
        person_instance = Person.people[person_dict["name"]]
        if person_dict.get("wife"):
            person_instance.wife = Person.people[person_dict["wife"]]
        elif person_dict.get("husband"):
            person_instance.husband = Person.people[person_dict["husband"]]

    return person_objects
