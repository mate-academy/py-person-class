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
        for credentials, person_info in person.items():
            if credentials == "husband" and person_info is not None:
                inst.husband = person_info
            if credentials == "wife" and person_info is not None:
                inst.wife = person_info
        person_list.append(inst)
    wife_husband(person_list)
    return person_list


def wife_husband(person_list: list) -> None:
    for person in person_list:
        for credentials, person_info in person.__dict__.items():
            if credentials == "husband":
                person.husband = Person.people[person_info]
            if credentials == "wife":
                person.wife = Person.people[person_info]
