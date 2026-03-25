class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = []

    for person in people:
        person_obj = Person(person["name"], person["age"])
        person_list.append(person_obj)

    for person in people:
        person_obj = Person.people.get(person["name"])

        if person_wife := person.get("wife"):
            person_obj.wife = Person.people[person_wife]

        if person_husband := person.get("husband"):
            person_obj.husband = Person.people[person_husband]

    return person_list
