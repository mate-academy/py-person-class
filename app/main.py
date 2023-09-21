class Person:
    people = {}

    def __init__(
            self,
            name: str,
            age: int
    ) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]

        person_list.append(Person(name, age))

    for person_data in people:
        name = person_data["name"]
        person = Person.people[name]

        wife_name = person_data.get("wife")
        husband_name = person_data.get("husband")

        if wife_name:
            person.wife = Person.people.get(wife_name)
        elif husband_name:
            person.husband = Person.people.get(husband_name)

    return person_list
