class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        wife = person.get("wife")
        if wife in Person.people:
            cur_person = Person.people[person["name"]]
            cur_person.wife = Person.people[wife]

        husband = person.get("husband")
        if husband in Person.people:
            cur_person = Person.people[person["name"]]
            cur_person.husband = Person.people[husband]

    return persons
