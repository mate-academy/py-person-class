class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result_list = []
    result_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if person.get("wife"):
            husband_obj = Person.people[person["name"]]
            wife_obj = Person.people[person["wife"]]
            husband_obj.wife = wife_obj

        if person.get("husband"):
            wife_obj = Person.people[person["name"]]
            husband_obj = Person.people[person["husband"]]
            wife_obj.husband = husband_obj

    return result_list
