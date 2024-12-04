class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(data["name"], data["age"]) for data in people]

    for data in people:
        person = Person.people[data["name"]]
        if (wife_name := data.get("wife")):
            person.wife = Person.people[wife_name]
            person.wife.husband = person
        if (husband_name := data.get("husband")):
            person.husband = Person.people[husband_name]
            person.husband.wife = person

    return person_list
