class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list[dict[str, str]]) -> list["Person"]:
    person_list = []

    # Create Person instances
    person_list = [Person(person_data["name"],
                          person_data["age"]) for person_data in people]

    for person_data in people:
        name = person_data["name"]
        spouse_name = (person_data.get("wife") or person_data.get("husband"))
        if spouse_name:
            spouse = Person.people.get(spouse_name)
            if spouse:
                if "wife" in person_data:
                    Person.people[name].wife = spouse
                spouse.husband = Person.people.get(name)

    return person_list
