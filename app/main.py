class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    persons = {}
    for person in people:
        person = Person(person["name"], person["age"])
        persons[person.name] = person
    for person in people:
        if person.get("wife", None) is not None:
            persons[person["name"]].wife = persons[person["wife"]]
        if person.get("husband", None) is not None:
            persons[person["name"]].husband = persons[person["husband"]]
    return [person for person in persons.values()]
