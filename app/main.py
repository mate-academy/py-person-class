class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:

    for person in people:
        per = Person(name=person["name"], age=person["age"])
        Person.people[person["name"]] = per

        if person.get("wife") is not None:
            per.wife = person["wife"]

        if person.get("husband") is not None:
            per.husband = person["husband"]

    for person in people:
        if (person.get("wife") is not None):
            husband = Person.people[person["name"]]
            husband.wife = Person.people[husband.wife]

        if (person.get("husband") is not None):
            wife = Person.people[person["name"]]
            wife.husband = Person.people[wife.husband]

    return [values for values in Person.people.values()]
