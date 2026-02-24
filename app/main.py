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


def create_person_list(people: list) -> list:

    Person.people.clear()

    people_ls = [
        Person(
            name=person.get("name"),
            age=person.get("age"),
        )
        for person in people
    ]

    for i, person in enumerate(people):

        wife_name = person.get("wife", None)
        if wife_name is not None:
            people_ls[i].wife = Person.people[wife_name]

        husband_name = person.get("husband", None)
        if husband_name is not None:
            people_ls[i].husband = Person.people[husband_name]

    return people_ls
