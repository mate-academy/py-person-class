class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_persons = []
    for dict_persons in people:
        person = Person(dict_persons["name"], dict_persons["age"])
        list_persons.append(person)

    for person in people:
        if person.get("husband"):
            Person.people[person["name"]].husband = \
                Person.people[person["husband"]]
        if person.get("wife"):
            Person.people[person["name"]].wife = Person.people[person["wife"]]
    return list_persons
