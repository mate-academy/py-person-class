class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()


    instances = [Person(d["name"], d["age"]) for d in people]

    for d in people:
        p = Person.people[d["name"]]
        wife_name = d.get("wife")
        husband_name = d.get("husband")

        if wife_name:
            p.wife = Person.people[wife_name]
        if husband_name:
            p.husband = Person.people[husband_name]

    return instances

