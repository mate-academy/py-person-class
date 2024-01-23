class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []
    for person_data in people:
        person_instance = Person(person_data["name"], person_data["age"])
        if "wife" in person_data and person_data["wife"] is not None:
            wife_instance = Person.people.get(person_data["wife"])
            if wife_instance is not None:
                person_instance.wife = wife_instance
                wife_instance.husband = person_instance
        elif "husband" in person_data and person_data["husband"] is not None:
            husband_instance = Person.people.get(person_data["husband"])
            if husband_instance is not None:
                person_instance.husband = husband_instance
                husband_instance.wife = person_instance
        person_instances.append(person_instance)
    return person_instances
