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

        wife_name = p_dict.get("wife")
        if wife_name is not None:
            setattr(person, "wife", Person.people[wife_name])

        husband_name = p_dict.get("husband")
        if husband_name is not None:
            setattr(person, "husband", Person.people[husband_name])
    return person_list
