class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(p["name"], p["age"]) for p in people]
    for person in people:
        person_obj = Person.people[person["name"]]
        wife_name = person.get("wife")
        husband_name = person.get("husband")

        if wife_name:
            person_obj.wife = Person.people[wife_name]
        elif husband_name:
            person_obj.husband = Person.people[husband_name]

    return person_list
