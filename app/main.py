class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_of_persons = []
    for person in people:
        new_persona = Person(person["name"], person["age"])
        list_of_persons.append(new_persona)
    for person in people:
        last_person = Person.people[person["name"]]
        if person.get("wife") is not None:
            last_person.wife = Person.people[person["wife"]]
        if person.get("husband") is not None:
            last_person.husband = Person.people[person["husband"]]
    return list_of_persons
