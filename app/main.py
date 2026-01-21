class Person:
    people = {}

    def __init__(
        self,
        name: str,
        age: int
    ) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(
    people: list[dict]
) -> list[Person]:
    person_list = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for person_index in range(len(people)):
        person = people[person_index]

        wife_name = person.get("wife")
        husband_name = person.get("husband")

        if wife_name is not None:
            person_list[person_index].wife = Person.people[wife_name]
        elif husband_name is not None:
            person_list[person_index].husband = Person.people[husband_name]

    return person_list
