class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = []

    for person in people:
        name = person["name"]
        age = person["age"]

        new_person = Person(name, age)
        person_list.append(new_person)

    for person in people:
        name = person["name"]
        new_person = Person.people[name]

        if person.get("wife") is not None:
            wife_name = person["wife"]
            new_person.wife = Person.people[wife_name]

        if person.get("husband") is not None:
            husband_name = person["husband"]
            new_person.husband = Person.people[husband_name]
    return person_list
