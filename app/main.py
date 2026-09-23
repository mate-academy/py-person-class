class Person:
    """class that represents a person with attributes"""
    def __init__(self, name: str, age: int) -> None :
        self.name = name
        self.age = age
        self.people[self.name] = self


Person.people = {}


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for people_dict, person_obj in zip(people, person_list):
        if people_dict.get("wife"):
            person_obj.wife = Person.people[people_dict["wife"]]
        if people_dict.get("husband"):
            person_obj.husband = Person.people[people_dict["husband"]]
    return person_list
