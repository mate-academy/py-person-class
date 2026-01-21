class Person:

    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people = {
        person["name"]: Person(person["name"], person["age"])
        for person in people
    }
    for person in people:
        if person.get("wife"):
            wife = Person.people[person["wife"]]
            husband = Person.people[person["name"]]
        elif person.get("husband"):
            husband = Person.people[person["husband"]]
            wife = Person.people[person["name"]]
        if wife and husband:
            wife.husband = husband
            husband.wife = wife

    return [Person.people[person["name"]] for person in people]
