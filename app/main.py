class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.husband = None
        self.wife = None
        Person.people[name] = self


def create_person_list(people: list) -> list:
    [Person(name=person["name"], age=person["age"]) for person in people]

    for i in people:
        person = Person.people[i["name"]]

        husband_name = i.get("husband")
        wife_name = i.get("wife")

        if husband_name:
            person.husband = Person.people[husband_name]
        if wife_name:
            person.wife = Person.people[wife_name]

        if person.husband is None:
            del person.husband
        if person.wife is None:
            del person.wife

    return list(Person.people.values())
