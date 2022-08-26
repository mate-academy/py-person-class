class Person:

    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result_list = []
    for person in people:
        result_list.append(Person(person["name"], person["age"]))
    for obj in result_list:
        for person in people:
            if obj.name == person["name"] and "husband" in person:
                if person["husband"] is not None:
                    obj.husband = Person.people[person["husband"]]
            if obj.name == person["name"] and "wife" in person:
                if person["wife"] is not None:
                    obj.wife = Person.people[person["wife"]]
    return result_list
