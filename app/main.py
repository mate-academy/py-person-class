class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    result = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        obj_to_change = Person.people[person["name"]]

        if "wife" in person and person["wife"]:
            wife_to_add = Person.people[person["wife"]]
            setattr(obj_to_change, "wife", wife_to_add)

        elif "husband" in person and person["husband"]:
            husband_to_add = Person.people[person["husband"]]
            setattr(obj_to_change, "husband", husband_to_add)

    return result
