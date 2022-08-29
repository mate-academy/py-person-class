class Person:

    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result_list = []
    for person in people:
        item = Person(person["name"], person["age"])
        if "husband" in person and person["husband"] is not None:
            item.husband = person["husband"]
        if "wife" in person and person["wife"] is not None:
            item.wife = person["wife"]
        result_list.append(item)
    for item in result_list:
        if hasattr(item, "husband"):
            item.husband = Person.people[item.husband]
        if hasattr(item, "wife"):
            item.wife = Person.people[item.wife]
    return result_list
