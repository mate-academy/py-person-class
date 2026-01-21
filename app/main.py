class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people = {}

    person_instances = []

    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person_instances.append(Person(name, age))

    for person_data in people:
        current_person_name = person_data["name"]
        current_person_obj = Person.people[current_person_name]

        if "wife" in person_data and person_data["wife"] is not None:
            wife_name = person_data["wife"]
            current_person_obj.wife = Person.people.get(wife_name)

        if "husband" in person_data and person_data["husband"] is not None:
            husband_name = person_data["husband"]
            current_person_obj.husband = Person.people.get(husband_name)

    return person_instances
