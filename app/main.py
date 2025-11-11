class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def set_wife(self, wife: "Person") -> None:
        self.wife = wife
        wife.husband = self

    def set_husband(self, husband: "Person") -> None:
        self.husband = husband
        husband.wife = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(persons["name"], persons["age"])
        for persons in people
    ]
    for persons in people:
        person = Person.people[persons["name"]]
        if persons.get("wife"):
            wife = Person.people[persons.get("wife")]
            person.set_wife(wife)
        elif persons.get("husband"):
            husband = Person.people[persons.get("husband")]
            person.set_husband(husband)
    return person_list
