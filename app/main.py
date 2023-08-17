class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person_data in people:
        exemplar = Person(
            person_data["name"],
            person_data["age"]
        )
        wife = person_data.get("wife")
        husband = person_data.get("husband")

        if wife and wife in Person.people:
            exemplar.wife = Person.people[wife]
            Person.people[wife].husband = exemplar

        elif husband and husband in Person.people:
            exemplar.husband = Person.people[husband]
            Person.people[husband].wife = exemplar

        person_list.append(exemplar)

    return person_list
