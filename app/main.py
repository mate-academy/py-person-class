
class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = []
    for man in people:
        person_list.append(Person(man["name"], man["age"]))

    for person in people:
        if person.get("wife") and Person.people.get(person["wife"]):
            Person.people[person["name"]].wife =\
                Person.people[person["wife"]]

        elif "husband" in person and person["husband"] in Person.people:
            Person.people[person["name"]].husband =\
                Person.people[person["husband"]]

    return person_list
