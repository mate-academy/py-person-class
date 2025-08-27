class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:

    person_instances = []

    for person_data in people:
        person_instance = Person(person_data["name"], person_data["age"])
        person_instances.append(person_instance)

    for person_data in people:
        name = person_data["name"]

        if "wife" in person_data and person_data["wife"] is not None:
            husband_instance = Person.people[name]
            wife_instance_name = person_data["wife"]
            wife_instance = Person.people[wife_instance_name]
            husband_instance.wife = wife_instance

        elif "husband" in person_data and person_data["husband"] is not None:
            wife_instance = Person.people[name]
            husband_instance_name = person_data["husband"]
            husband_instance = Person.people[husband_instance_name]
            wife_instance.husband = husband_instance

    return person_instances
