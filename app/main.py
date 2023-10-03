class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list: [Person] = [
        Person(name=person["name"], age=person["age"])
        for person in people
    ]

    # Adding husband and wife for people
    for person in people:
        if isinstance(person.get("husband"), str):
            person_obj = Person.people[person["name"]]
            husband_obj = Person.people[person["husband"]]
            person_obj.husband = husband_obj

        if isinstance(person.get("wife"), str):
            person_obj = Person.people[person["name"]]
            wife_obj = Person.people[person["wife"]]
            person_obj.wife = wife_obj

    return person_list
