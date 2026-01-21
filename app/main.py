class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.spouse = None
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        Person(name, age)

    for person_data in people:
        person = Person.people[person_data["name"]]

        if "wife" in person_data and person_data["wife"]:
            person.wife = Person.people.get(person_data["wife"])
            if person.wife:
                person.wife.husband = person

        if "husband" in person_data and person_data["husband"]:
            person.husband = Person.people.get(person_data["husband"])
            if person.husband:
                person.husband.wife = person

    return list(Person.people.values())
