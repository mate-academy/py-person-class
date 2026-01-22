class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    [Person(data_person["name"], data_person["age"]) for data_person in people]

    for person_dict in people:
        person_name = person_dict["name"]
        person = Person.people[person_name]

        wife_name = person_dict.get("wife")
        if wife_name and wife_name in Person.people:
            person.wife = Person.people[wife_name]

        husband_name = person_dict.get("husband")
        if husband_name and husband_name in Person.people:
            person.husband = Person.people[husband_name]

    return [Person.people[person_dict["name"]] for person_dict in people]
