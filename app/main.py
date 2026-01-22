class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = [Person(data["name"], data["age"]) for data in people]

    for data in people:
        person = Person.people[data["name"]]

        wife_name = data.get("wife")
        husband_name = data.get("husband")

        if wife_name:
            person.wife = Person.people.get(wife_name)

        if husband_name:
            person.husband = Person.people.get(husband_name)

    return persons
