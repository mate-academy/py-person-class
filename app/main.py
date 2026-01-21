class Person:
    people = {}

    def __init__(self, name: str, age: str) -> any:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        each_person = Person(name=person["name"], age=person["age"])
        person_list.append(each_person)
    for person in people:
        if person.get("wife"):
            each_person.wife = Person.people[person["wife"]]
            each_person.wife.husband = each_person
        elif person.get("husband"):
            each_person.husband = Person.people[person["husband"]]
            each_person.husband.wife = each_person
    return person_list
