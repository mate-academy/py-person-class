class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for data in people:
        name = data["name"]
        age = data["age"]
        wife = data.get("wife")
        husband = data.get("husband")

        person = Person(name, age)
        person_list.append(person)

        if wife is not None:
            if wife in Person.people:
                person.wife = Person.people[wife]
                Person.people[wife].husband = person

        if husband is not None:
            if husband in Person.people:
                person.husband = Person.people[husband]
                Person.people[husband].wife = person

        if person.wife is None:
            del person.wife

    return person_list
