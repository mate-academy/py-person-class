class Person:

    people = {}

    def __init__(self, name: str, age: float) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    res_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        if wife_name := person.get("wife"):
            res_list[person].wife = Person.people.get(wife_name)
        elif husband_name := person.get("husband"):
            res_list[person].husband = Person.people.get(husband_name)

    return res_list
