class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        profile = Person(person["name"], person["age"])
        person_list.append(profile)

        if person.get("wife"):
            wife_name = person["wife"]
            if wife_name in Person.people:
                wife = Person.people[person["wife"]]
                profile.wife = wife
                wife.husband = profile

        if person.get("husband"):
            husband_name = person["husband"]
            if husband_name in Person.people:
                husband = Person.people[person["husband"]]
                profile.husband = husband
                husband.wife = profile

    return person_list
