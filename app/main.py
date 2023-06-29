class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people.update({name: self})


def create_person_list(people: list) -> list:
    list_of_persons = [
        Person(person["name"], person["age"])
        for person in people
    ]
    for person in people:
        if person.get("wife"):
            Person.people[person["name"]].wife = \
                Person.people[person["wife"]]
        elif person.get("husband"):
            Person.people[person["name"]].husband = \
                Person.people[person["husband"]]
    return list_of_persons
