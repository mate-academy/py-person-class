class Person:

    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result_list = []
    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])
        if "husband" in person_dict and person_dict["husband"] is not None:
            person.husband = person_dict["husband"]
        if "wife" in person_dict and person_dict["wife"] is not None:
            person.wife = person_dict["wife"]
        result_list.append(person)
    for person in result_list:
        if hasattr(person, "husband"):
            person.husband = Person.people[person.husband]
        if hasattr(person, "wife"):
            person.wife = Person.people[person.wife]
    return result_list
