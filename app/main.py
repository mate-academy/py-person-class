class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    result = [
        Person(
            person_data.get("name"),
            person_data.get("age")
        )
        for person_data in people
    ]

    for person_data in people:
        person = Person.people.get(person_data.get("name"))
        wife_name = person_data.get("wife")
        husband_name = person_data.get("husband")

        wife = Person.people.get(wife_name)
        husband = Person.people.get(husband_name)

        if wife:
            person.wife = wife
        if husband:
            person.husband = husband

    return result
