class Person:
    people = {}

    def __init__(self, name: str, age: int) -> dict:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(
            someone["name"],
            someone["age"]
        ) for someone in people
    ]

    for someone in people:
        person = Person.people[someone["name"]]
        if someone.get("wife") is not None:
            wife_name = someone["wife"]
            wife = Person.people[wife_name]
            person.wife = wife
            wife.husband = person
        elif someone.get("husband") is not None:
            husband_name = someone["husband"]
            husband = Person.people[husband_name]
            person.husband = husband
            husband.wife = person

    return person_list
