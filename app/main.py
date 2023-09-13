class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list:
    list_instances = [
        Person(person["name"], person["age"]) for person in people
    ]

    for person in people:
        if person.get("wife"):
            person_name = person["name"]
            wife_name = person["wife"]
            Person.people[person_name].wife = Person.people.get(wife_name)
        if person.get("husband"):
            person_name = person["name"]
            husband_name = person["husband"]
            Person.people[person_name].husband = (
                Person.people.get(husband_name)
            )
    return list_instances
