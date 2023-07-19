class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list[dict[str, str]]) -> list["Person"]:
    person_list = []
    person_dict = {}

    # Create Person instances
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        person_list.append(person)

        person_dict[name] = person

        # Add wife/husband attributes
        for person_data in people:
            name = person_data["name"]
            spouse_name = (person_data.get("wife")
                           or person_data.get("husband"))
            if spouse_name:
                spouse = person_dict.get(spouse_name)

                if spouse:
                    if "wife" in person_data:
                        person_dict[name].wife = spouse
                    spouse.husband = person_dict.get(name)

    return person_list
