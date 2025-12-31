class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    person_list = [Person(p.get("name"), p.get("age")) for p in people]

    for p_dict in people:
        current_person = Person.people.get(p_dict.get("name"))

        wife_name = p_dict.get("wife")
        husband_name = p_dict.get("husband")

        if wife_name and Person.people.get(wife_name):
            current_person.wife = Person.people.get(wife_name)  # type: ignore

        if husband_name and Person.people.get(husband_name):
            current_person.husband = Person.people.get(husband_name)

    return person_list
