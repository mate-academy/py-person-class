class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self


def create_person_list(people_data: list[dict]) -> list[Person]:
    # First pass: create all Person instances with initialized attributes
    for person_data in people_data:
        name = person_data["name"]
        age = person_data["age"]
        Person(name, age)

    # Second pass: set relationships and clean up None values
    for person_data in people_data:
        name = person_data["name"]
        person_instance = Person.people[name]

        # Handle wife relationship
        if "wife" in person_data:
            if person_data["wife"] is not None:
                wife_name = person_data["wife"]
                wife_instance = Person.people[wife_name]
                person_instance.wife = wife_instance
            else:
                delattr(person_instance, "wife")  # Remove attribute if None

        # Handle husband relationship
        if "husband" in person_data:
            if person_data["husband"] is not None:
                husband_name = person_data["husband"]
                husband_instance = Person.people[husband_name]
                person_instance.husband = husband_instance
            else:
                delattr(person_instance, "husband")  # Remove attribute if None

    return [Person.people[person_data["name"]] for person_data in people_data]
