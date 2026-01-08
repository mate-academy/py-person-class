class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    result = [Person(d.get("name"), d.get("age")) for d in people]
    name_to_person = {p.name: p for p in result}

    for person_dict in people:
        person_name = person_dict.get("name")
        person = name_to_person.get(person_name)

        wife_name = person_dict.get("wife")
        if wife_name:
            person.wife = name_to_person.get(wife_name)

        husband_name = person_dict.get("husband")
        if husband_name:
            person.husband = name_to_person.get(husband_name)

    return result
