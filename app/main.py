class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.spouse = None
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for human in people:
        name = human["name"]
        age = human["age"]
        Person(name, age)

    for human in people:
        person = Person.people[human["name"]]
        spouse_name = human.get("wife") or human.get("husband")
        if spouse_name:
            person.spouse = Person.people[spouse_name]
            if "wife" in human:
                person.wife = person.spouse
            elif "husband" in human:
                person.husband = person.spouse
    return list(Person.people.values())
