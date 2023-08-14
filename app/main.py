class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for i in people:
        person = Person(i.get("name"), i.get("age"))
        person_list.append(person)
    for person in people:
        if person.get("wife") is not None:
            name_wife = person.get("wife")
            Person.people[person["name"]].wife = Person.people[name_wife]
        elif person.get("husband") is not None:
            name_husband = person.get("husband")
            Person.people[person["name"]].husband = Person.people[name_husband]
    return person_list
