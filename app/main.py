class Person:

    people = {}

    def __init__(
            self,
            name: str,
            age: int
    ) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    result = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        person_obj = Person.people[person["name"]]
        if person.get("wife") is not None:
            wife_obj = Person.people[person["wife"]]
            person_obj.wife = wife_obj
            wife_obj.husband = person_obj
        elif person.get("husband") is not None:
            husband_obj = Person.people[person["husband"]]
            person_obj.husband = husband_obj
            husband_obj.wife = person_obj

    return result
