class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = []

    for person in people:
        instance = Person(person["name"], person["age"])

        if "wife" in person and person["wife"]:
            instance.wife = Person.people.get(person["wife"])
            if instance.wife:
                instance.wife.husband = instance
        if "husband" in person and person["husband"]:
            instance.husband = Person.people.get(person["husband"])
            if instance.husband:
                instance.husband.wife = instance
        person_list.append(instance)

    return person_list
