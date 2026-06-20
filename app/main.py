class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        person_list.append(Person(person.get("name"), person.get("age")))

    for person in people:
        person_obj = Person.people[person.get("name", "")]

        wife_name = person.get("wife")
        if wife_name is not None and wife_name in Person.people:
            person_obj.wife = Person.people[wife_name]

        husband_name = person.get("husband")
        if husband_name is not None and husband_name in Person.people:
            person_obj.husband = Person.people[husband_name]

    return person_list
