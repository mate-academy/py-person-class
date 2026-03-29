class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    instances = [
        Person(p.get("name"), p.get("age"))
        for p in people
    ]

    for person_dict in people:
        name = person_dict.get("name")
        person_instance = Person.people.get(name)

        wife_name = person_dict.get("wife")
        husband_name = person_dict.get("husband")

        if wife_name:
            person_instance.wife = Person.people.get(wife_name)

        if husband_name:
            person_instance.husband = Person.people.get(husband_name)

    return instances
