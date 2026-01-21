class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    result = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        person_inst = Person.people[person["name"]]
        wife = Person.people.get(person.get("wife"))
        husband = Person.people.get(person.get("husband"))

        if wife:
            person_inst.wife = wife
            wife.husband = person_inst

        if husband:
            person_inst.husband = husband
            husband.wife = person_inst

    return result
