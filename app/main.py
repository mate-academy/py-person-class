class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(person["name"], person["age"]))

        wife_name = person.get("wife")
        husband_name = person.get("husband")

        if wife_name:
            person_list.wife = Person.people.get(wife_name)
        if husband_name:
            person_list.husband = Person.people.get(husband_name)
    return person_list
