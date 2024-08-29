class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []

    for person in people:
        name = person["name"]
        age = person["age"]
        person_instance = Person(name, age)
        person_instances.append(person_instance)

    for person in people:
        person_instance = Person.people[person["name"]]

        wife = person.get("wife")
        husband = person.get("husband")

        if wife:
            person_instance.wife = Person.people.get(wife)
            Person.people[wife].husband = person_instances

        if husband:
            person_instance.husband = Person.people.get(husband)
            Person.people[husband].wife = person_instance

    return person_instances
