class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[self.name] = self


def create_person_list(people_data: list) -> list:
    Person.people = {}
    person_list = []

    for person_dict in people_data:
        person = Person(person_dict["name"], person_dict["age"])
        person_list.append(person)

    for person_dict in people_data:
        name = person_dict["name"]
        current_person = Person.people[name]

        wife_name = person_dict.get("wife")
        if wife_name:
            wife = Person.people.get(wife_name)
            if wife:
                current_person.wife = wife
            else:
                print(
                    f"Warning: Wife \"{wife_name}\" for \"{name}\" "
                    "was not found in input data."
                )

        husband_name = person_dict.get("husband")
        if husband_name:
            husband = Person.people.get(husband_name)
            if husband:
                current_person.husband = husband
            else:
                print(
                    f"Warning: Husband \"{husband_name}\" for \"{name}\" "
                    "was not found in input data."
                )

    return person_list