import logging

# Configure logging
logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s")


class Person:
    people = {}  # Dictionary to store instances by name

    def __init__(self, name: str, age: int) -> None:
        if name in Person.people:
            raise ValueError(
                f"Person with name '{name}' already exists."
            )
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self

    def __repr__(self) -> str:
        return f"Person(name='{self.name}', age={self.age})"


def create_person_list(data: list) -> list:
    # Clear existing people to avoid conflicts
    Person.people.clear()
    person_list = []

    seen_names = set()
    for person in data:
        name = person["name"]
        if name in seen_names:
            logging.error(
                f"Duplicate name detected: '{name}'. Skipping entry."
            )
            continue
        seen_names.add(name)

    # First, create all Person instances
    for person in data:
        name, age = person["name"], person["age"]
        try:
            person_obj = Person(name, age)
            person_list.append(person_obj)
        except ValueError as e:
            logging.error(e)

    # Second, assign relationships
    for person in data:
        instance = Person.people.get(person["name"])
        if not instance:
            continue  # Skip if the person wasn't created

        if "wife" in person and person["wife"]:
            wife_name = person["wife"]
            instance.wife = Person.people.get(wife_name)
            if instance.wife is None:
                logging.warning(
                    f"Wife '{wife_name}' not found for '{instance.name}'."
                )

        if "husband" in person and person["husband"]:
            husband_name = person["husband"]
            instance.husband = Person.people.get(husband_name)
            if instance.husband is None:
                logging.warning(
                    f"Husband '{husband_name}' not found for '{instance.name}'."
                )

    return person_list
