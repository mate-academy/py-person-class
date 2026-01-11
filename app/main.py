
class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    name_map = {p.name: p for p in person_list}
    for person in people:
        obj = name_map[person["name"]]
        wife_name = person.get("wife")

        if wife_name is not None and wife_name in name_map:
            obj.wife = name_map[wife_name]

        husband_name = person.get("husband")
        if husband_name is not None and husband_name in name_map:
            obj.husband = name_map[husband_name]

    return person_list
