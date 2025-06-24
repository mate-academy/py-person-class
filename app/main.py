class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    person_list = []
    for pe in people:
        person = Person(name=pe["name"], age=pe["age"])
        person_list.append(person)

    for i, pe in enumerate(people):
        person = person_list[i]

        if "wife" in pe and pe["wife"] is not None:
            person.wife = Person.people[pe["wife"]]
        if "husband" in pe and pe["husband"] is not None:
            person.husband = Person.people[pe["husband"]]
    return person_list
