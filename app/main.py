class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people = {}

    people_list = [
        Person(name=person["name"], age=person["age"])
        for person in people
    ]

    for index, person in enumerate(people):
        wife_name = person.get("wife")
        husband_name = person.get("husband")
        if wife_name is not None:
            people_list[index].wife = Person.people.get(wife_name)
        if husband_name is not None:
            people_list[index].husband = Person.people.get(husband_name)

    return people_list
