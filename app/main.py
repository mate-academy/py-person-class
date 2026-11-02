class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        person_instance = Person.people[person["name"]]
        wife_name = person.get("wife")
        husband_name = person.get("husband")
        wife = Person.people.get(wife_name)
        husband = Person.people.get(husband_name)

        if wife is not None:
            person_instance.wife = wife
        if husband is not None:
            person_instance.husband = husband

    return person_list
