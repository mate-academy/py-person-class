class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    @classmethod
    def reset_people(cls) -> None:
        cls.people.clear()


def create_person_list(people: list) -> list:
    Person.reset_people()

    person_instances = []
    for person_data in people:
        # Create a new Person instance
        person = Person(name=person_data["name"], age=person_data["age"])
        person_instances.append(person)

    for person_data in people:
        person = Person.people[person_data["name"]]
        if "wife" in person_data and person_data["wife"] is not None:
            person.wife = Person.people.get(person_data["wife"])
        elif "husband" in person_data and person_data["husband"] is not None:
            person.husband = Person.people.get(person_data["husband"])

    return person_instances
