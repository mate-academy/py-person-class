class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list[Person]) -> list[Person]:
    result = [Person(name=person["name"],
                     age=person["age"]) for person in people]

    for person in people:
        current_person = Person.people[person["name"]]
        if wife_name := person.get("wife"):
            current_person.wife = Person.people[wife_name]
        elif husband_name := person.get("husband"):
            current_person.husband = Person.people[husband_name]
    return result
