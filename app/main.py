class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    person_list = [
        Person(person.get("name"), person.get("age"))
        for person in people
    ]

    for person_dict in people:
        person = Person.people.get(person_dict.get("name"))

        wife_name = person_dict.get("wife")
        if wife_name:
            person.wife = Person.people.get(wife_name)

        husband_name = person_dict.get("husband")
        if husband_name:
            person.husband = Person.people.get(husband_name)

    return person_list
