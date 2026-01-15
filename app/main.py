class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    person_list = [Person(person_data["name"], person_data["age"])
                   for person_data in people]

    for i, person_data in enumerate(people):
        person = person_list[i]

        wife_name = person_data.get("wife")
        wife_person = Person.people.get(wife_name)
        if wife_name is not None and wife_person is not None:
            person.wife = wife_person

        husband_name = person_data.get("husband")
        husband_person = Person.people.get(husband_name)
        if husband_name is not None and husband_person is not None:
            person.husband = husband_person

    return person_list
