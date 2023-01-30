class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    persons = []

    for one_person in people:
        persons.append(Person(one_person["name"], one_person["age"]))

    for person in persons:
        for one_person in people:
            if person.name == \
                    one_person.get("name") and one_person.get("wife"):
                person.wife = Person.people.get(one_person.get("wife"))
            if person.name == \
                    one_person.get("name") and one_person.get("husband"):
                person.husband = Person.people.get(one_person.get("husband"))

    return persons
