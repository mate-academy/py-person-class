class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list[Person]:
    person_list = [Person(person["name"], person["age"])
                   for person in people]

    for person in people:
        wife_key = person.get("wife")
        husband_key = person.get("husband")
        if wife_key is not None:
            Person.people[person["name"]].wife = Person.people[wife_key]
        if husband_key is not None:
            Person.people[person["name"]].husband = Person.people[husband_key]

    return person_list
