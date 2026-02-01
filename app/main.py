class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    person_list = [Person(atr["name"], atr["age"]) for atr in people]
    for atr in people:
        person = Person.people[atr["name"]]
        wife_name = atr.get("wife")
        if wife_name is not None:
            person.wife = Person.people[wife_name]
        husband_name = atr.get("husband")
        if husband_name is not None:
            person.husband = Person.people[husband_name]
    return person_list
