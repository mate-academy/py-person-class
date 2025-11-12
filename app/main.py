class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()
    person_list = [Person(human["name"], human["age"]) for human in people]
    for human in people:
        person = Person.people[human["name"]]
        wife_name = human.get("wife")
        husband_name = human.get("husband")

        if wife_name:
            person.wife = Person.people[wife_name]
        if husband_name:
            person.husband = Person.people[husband_name]

    return person_list
