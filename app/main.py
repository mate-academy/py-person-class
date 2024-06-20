class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list[dict]) -> list[Person]:
    add_persons_to_people(people)
    return add_husband_and_wife(people)


def add_persons_to_people(people: list[dict]) -> None:
    for person in people:
        Person.people[person["name"]] = Person(person["name"], person["age"])


def add_husband_and_wife(people: list[dict]) -> list[Person]:
    result = []
    for person in people:
        created_person = Person(person["name"], person["age"])
        if person.get("wife") is not None:
            created_person.wife = Person.people[person["wife"]]
            Person.people[person["wife"]].husband = created_person

        result.append(created_person)

    return result
