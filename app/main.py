class Person:

    people = {}

    def __init__(self, name: int, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        inst = Person(name=person["name"], age=person["age"])
        for key, value in person.items():
            if key == "husband" and value is not None:
                inst.husband = value
            if key == "wife" and value is not None:
                inst.wife = value
        person_list.append(inst)
    wife_husband(person_list)
    return person_list


def wife_husband(person_list: list) -> None:
    for person in person_list:
        for key, value in person.__dict__.items():
            if key == "husband":
                person.husband = Person.people[value]
            if key == "wife":
                person.wife = Person.people[value]
