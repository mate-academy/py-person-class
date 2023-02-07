class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])
        person_list.append(person)

    for person in people:
        if person.get("wife"):
            value_wife = Person.people[person["wife"]]
            Person.people[person["name"]].wife = value_wife
        if person.get("husband"):
            value_husband = Person.people[person["husband"]]
            Person.people[person["name"]].husband = value_husband
    return person_list
