class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:

    Person.people.clear()

    # Pass 1: Instantiate every Person and save to a new list
    person_list = [Person(p["name"], p["age"]) for p in people]

    # Pass 2: Link wife/husband attributes
    for p_dict in people:
        person = Person.people[p_dict["name"]]

        # Link wife if present and not None
        if "wife" in p_dict and p_dict["wife"] is not None:
            wife_name = p_dict["wife"]
            setattr(person, "wife", Person.people[wife_name])

        # Link husband if present and not None
        if "husband" in p_dict and p_dict["husband"] is not None:
            husband_name = p_dict["husband"]
            setattr(person, "husband", Person.people[husband_name])

    # MUST return the list of Person instances
    return person_list
