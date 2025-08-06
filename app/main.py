class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()  # <-- Clear previous Person instances here

    # First, create all Person instances without wife/husband links
    for person_data in people:
        Person(person_data["name"], person_data["age"])

    # Now, set wife/husband attributes if not None
    for person_data in people:
        person_instance = Person.people[person_data["name"]]
        spouse_key = None
        if "wife" in person_data:
            spouse_key = "wife"
        elif "husband" in person_data:
            spouse_key = "husband"

        if spouse_key and person_data[spouse_key] is not None:
            spouse_instance = Person.people[person_data[spouse_key]]
            setattr(person_instance, spouse_key, spouse_instance)

    # Return list of Person instances in original input order
    return [Person.people[person_data["name"]] for person_data in people]
