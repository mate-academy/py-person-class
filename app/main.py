class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.spouse = None
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_instances = []
    for person_info in people:
        name = person_info["name"]
        age = person_info["age"]
        person = Person(name, age)
        spouse_name = person_info.get("wife") or person_info.get("husband")
        if spouse_name:
            if spouse_name in Person.people:
                spouse = Person.people[spouse_name]
                person.spouse = spouse
                spouse.spouse = person
            else:
                pass

        person_instances.append(person)
    return person_instances
