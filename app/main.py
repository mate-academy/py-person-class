class Person:
    # Class attribute to store instances by their name
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        # Add the instance to the people dictionary
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # First pass: Create all Person instances
    person_instances = []
    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        person_instances.append(Person(name, age))

    # Second pass: Link spouses
    for person_dict in people:
        person = Person.people[person_dict["name"]]
        spouse_key = "wife" if "wife" in person_dict else "husband"
        spouse_name = person_dict.get(spouse_key)
        if spouse_name:
            spouse_instance = Person.people.get(spouse_name)
            if spouse_key == "wife":
                person.wife = spouse_instance
            elif spouse_key == "husband":
                person.husband = spouse_instance

    return person_instances


def clear_people() -> None:
    Person.people.clear()
