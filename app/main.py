class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for entity in people:
        person = Person(entity["name"], entity["age"])
        if entity.get("wife"):
            wife = Person.people.get(entity["wife"])
            if wife:
                person.wife = wife
                wife.husband = person
        elif entity.get("husband"):
            husband = Person.people.get(entity["husband"])
            if husband:
                person.husband = husband
                husband.wife = person
        person_list.append(person)

    return person_list
