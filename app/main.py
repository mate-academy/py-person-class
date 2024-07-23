class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        wife_name = person.get("wife")
        husband_name = person.get("husband")
        person_obj = Person.people[person["name"]]

        if wife_name:
            person_obj.wife = Person.people[wife_name]
        if husband_name:
            person_obj.husband = Person.people[husband_name]

    return person_list
