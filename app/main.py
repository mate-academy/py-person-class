class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.people[name] = self


def set_family_link(status: str, person: dict) -> None:
    people_dict = Person.people
    if status in person and person[status] in people_dict:
        setattr(people_dict[person["name"]],
                status, people_dict[person[status]])


def create_person_list(people: list[dict]) -> list[Person]:
    wife, husband = "wife", "husband"
    persons = [Person(person["name"], person["age"])
               for person in people]
    for person in people:
        set_family_link(wife, person)
        set_family_link(husband, person)
    return persons
