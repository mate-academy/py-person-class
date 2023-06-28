class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.people[self.name] = self


def set_family_link(status: str, person: dict) -> None:
    if status in person.keys() \
            and person[status] in Person.people.keys():
        setattr(Person.people[person["name"]],
                status, Person.people[person[status]])


def create_person_list(people: list[dict]) -> list[Person]:
    wife, husband = "wife", "husband"
    persons = []
    for person_info in people:
        appended_person = Person(person_info["name"], person_info["age"])
        persons.append(appended_person)

    for person in people:
        set_family_link(wife, person)
        set_family_link(husband, person)
    return persons
