class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(
        data: list,
        wife_key: str = "wife",
        husband_key: str = "husband"
) -> list:
    person_list = [Person(person_data["name"],
                   person_data["age"]) for person_data in data]

    for person_data in data:
        person = Person.people[person_data["name"]]

        if person_data.get(wife_key) is not None:
            wife_id = person_data.get(wife_key)
            person.wife = Person.people.get(wife_id, None)

        if person_data.get(husband_key) is not None:
            husband_id = person_data.get(husband_key)
            person.husband = Person.people.get(husband_id, None)

    return person_list
