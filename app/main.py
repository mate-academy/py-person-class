class Person:
    people = {}

    def __init__(
            self,
            name: str,
            age: int = None
    ) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person_data in people:
        name = person_data["name"]
        age = person_data.get("age")
        person_list.append(Person(name, age))

    for person_data in people:
        name = person_data["name"]
        person = Person.people[name]

        wife_name = person_data.get("wife")
        if wife_name:
            person.wife = Person.people.get(wife_name)

        husband_name = person_data.get("husband")
        if husband_name:
            person.husband = Person.people.get(husband_name)

    return person_list
