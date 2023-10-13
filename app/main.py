class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for single_person in people:
        if single_person.get("wife"):
            person = Person.people[single_person["name"]]
            wife = Person.people.get(single_person["wife"])
            person.wife = wife

        if single_person.get("husband"):
            person = Person.people[single_person["name"]]
            husband = Person.people.get(single_person["husband"])
            person.husband = husband

    return person_list
