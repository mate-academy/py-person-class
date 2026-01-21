class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None

        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []

    for person in people:
        name = person["name"]
        age = person["age"]
        person_instance = Person(name, age)
        person_instances.append(person_instance)

    for person in people:
        name = person["name"]
        person_instance = Person.people[name]

        if "wife" in person:
            spouse_name = person["wife"]
            if spouse_name:
                person_instance.wife = Person.people.get(spouse_name)

        if "husband" in person:
            spouse_name = person["husband"]
            if spouse_name:
                person_instance.husband = Person.people.get(spouse_name)

    return person_instances
