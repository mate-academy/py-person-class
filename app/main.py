class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for data in people:
        name = data["name"]
        age = data["age"]
        wife = data.get("wife")

        person = Person(name, age)
        person_list.append(person)

        if wife and wife in Person.people:
            person.wife = Person.people[wife]
            Person.people[wife].husband = person

    return person_list
