class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_instances = []
    for person_data in people:
        person = Person(person_data["name"], person_data["age"])
        if person_data.get("wife"):
            person.wife = Person.people.get(person_data["wife"])
            if person.wife:
                person.wife.husband = person
        elif person_data.get("husband"):
            person.husband = Person.people.get(person_data["husband"])
            if person.husband:
                person.husband.wife = person
        person_instances.append(person)
    return person_instances
