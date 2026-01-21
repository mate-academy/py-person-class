class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    result: list[Person] = []

    for data in people:
        person = Person(data["name"], data["age"])
        result.append(person)

    for data, person in zip(people, result):
        wife_name = data.get("wife")

        if wife_name is not None:
            person.wife = Person.people.get(wife_name)

        husband_name = data.get("husband")

        if husband_name is not None:
            person.husband = Person.people.get(husband_name)

    return result
