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

        wife_name = person_data.get("wife")
        husband_name = person_data.get("husband")

        if wife_name is not None:
            wife_instance = Person.people.get(wife_name)
            if wife_instance is not None:
                person_instance.wife = wife_instance
                wife_instance.husband = person_instance
        elif husband_name is not None:
            husband_instance = Person.people.get(husband_name)
            if husband_instance is not None:
                person_instance.husband = husband_instance
                husband_instance.wife = person_instance

        person_instances.append(person_instance)

    return person_instances
