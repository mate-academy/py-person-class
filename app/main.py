class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    instances = []

    for person in people:
        instance = Person(person["name"], person["age"])
        if person.get("wife") is not None:
            instance.wife = Person.people.get(person["wife"])
        if person.get("husband") is not None:
            instance.husband = Person.people.get(person["husband"])
        instances.append(instance)

    for instance in instances:
        if hasattr(instance, "wife") and instance.wife:
            instance.wife.husband = instance
        if hasattr(instance, "husband") and instance.husband:
            instance.husband.wife = instance

    return instances
