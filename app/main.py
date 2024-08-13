class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    for person in people:
        instance = Person(name=person["name"], age=person["age"])
        Person.people[instance.name] = instance

    for dict_person in people:
        if dict_person.get("wife"):
            Person.people[dict_person["name"]].wife = Person.people[dict_person["wife"]]
        elif dict_person.get("husband"):
            Person.people[dict_person["name"]].husband = Person.people[dict_person["husband"]]

    return list(Person.people.values())
