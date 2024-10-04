class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        person_name = Person.people[person["name"]]
        wife = person.get("wife")
        husband = person.get("husband")

        if wife:
            person_name.wife = Person.people[wife]
        if husband:
            person_name.husband = Person.people[husband]

    return person_list
