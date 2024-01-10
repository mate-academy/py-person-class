class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    people_instances = [
        Person(person_dict["name"], person_dict["age"])
        for person_dict in people
    ]

    for person_dict in people:
        person = Person.people[person_dict["name"]]
        if "wife" in person_dict:
            wife_name = person_dict["wife"]
            if wife_name in Person.people:
                person.wife = Person.people[wife_name]
        if "husband" in person_dict:
            husband_name = person_dict["husband"]
            if husband_name in Person.people:
                person.husband = Person.people[husband_name]

    return people_instances
