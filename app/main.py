class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list:

    wife_or_husband = {}

    for person in people:
        person_name = person.get("name")
        Person(name=person_name, age=person.get("age"))

        if wife := person.get("wife"):
            wife_or_husband[person_name] = {"wife": wife}
            continue

        if husband := person.get("husband"):
            wife_or_husband[person_name] = {"husband": husband}

    people_instances = Person.people.values()

    for person, partner in wife_or_husband.items():
        if wife := partner.get("wife"):
            Person.people[person].wife = Person.people[wife]
            continue

        if husband := partner.get("husband"):
            Person.people[person].husband = Person.people[husband]

    return list(people_instances)
