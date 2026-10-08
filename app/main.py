class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    people_instances: list[Person] = []

    for person in people:
        person_instance = Person(person["name"], person["age"])
        people_instances.append(person_instance)

    for person in people:
        person_instance = Person.people[person["name"]]

        wife = person.get("wife")
        husband = person.get("husband")

        if wife:
            person_instance.wife = Person.people[wife]

        if husband:
            person_instance.husband = Person.people[husband]

    return people_instances
