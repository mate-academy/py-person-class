class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(name=p["name"], age=p["age"]) for p in people]

    for person in people:
        if person.get("wife") is not None:
            husband_obj = Person.people[person["name"]]
            wife_obj = Person.people[person["wife"]]
            husband_obj.wife = wife_obj
        elif person.get("husband") is not None:
            wife_obj = Person.people[person["name"]]
            husband_obj = Person.people[person["husband"]]
            wife_obj.husband = husband_obj
    return person_list
