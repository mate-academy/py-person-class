class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person_data in people:
        person = Person(
            person_data["name"],
            person_data["age"]
        )
        wife = person_data.get("wife")
        husband = person_data.get("husband")

        if wife and wife in Person.people:
            person.wife = Person.people[wife]
            Person.people[wife].husband = person

        elif husband and husband in Person.people:
            person.husband = Person.people[husband]
            Person.people[husband].wife = person

        person_list.append(person)

    return person_list
