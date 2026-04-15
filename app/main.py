class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(p["name"], p["age"]) for p in people]
    persons = Person.people
    for i_person in people:
        if i_person.get("wife") is not None:
            persons[i_person["name"]].wife = persons[i_person["wife"]]
        elif i_person.get("husband") is not None:
            persons[i_person["name"]].husband = persons[i_person["husband"]]
    return person_list
