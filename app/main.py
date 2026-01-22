class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = [
        Person(person["name"],
               person["age"])
        for person in people
    ]

    for person_info in people:
        name = person_info["name"]

        if person_info.get("wife"):
            wife_name = person_info["wife"]
            Person.people[name].wife = Person.people.get(wife_name)
        elif person_info.get("husband"):
            husband_name = person_info["husband"]
            Person.people[name].husband = Person.people.get(husband_name)

    return person_instances
