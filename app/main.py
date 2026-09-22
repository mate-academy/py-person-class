class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.add_people()

    def add_people(self) -> None:
        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    person_list = []

    for person in people:

        person_to_ad = Person(person["name"], person["age"])
        if person.get("wife"):
            person_to_ad.wife = person["wife"]
        elif person.get("husband"):
            person_to_ad.husband = person["husband"]
        person_list.append(person_to_ad)

    for person in person_list:
        if "wife" in person.__dict__:
            wife = Person.people.get(person.wife)

            if wife:
                person.wife = wife

        elif "husband" in person.__dict__:
            husband = Person.people.get(person.husband)

            if husband:
                person.husband = husband

    return person_list
