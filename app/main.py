class Person:
    people: dict = {}

    def __init__(
            self,
            name: str,
            age: int
    ) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list:
    result = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        wife_name = person.get("wife")
        husband_name = person.get("husband")

        if wife_name:
            Person.people[person["name"]].wife = Person.people[wife_name]
        elif husband_name:
            Person.people[person["name"]].husband = Person.people[husband_name]

    return result
