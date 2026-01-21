class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = []
    for person in people:
        name = person.get("name")
        age = person.get("age")
        person = Person(name, age)
        people_list.append(person)
    for person in people:
        person0 = Person.people[person["name"]]

        if "wife" in person and person["wife"]:
            wife = Person.people.get(person["wife"])
            if wife:
                person0.wife = wife
                wife.husband = person0

        if "husband" in person and person["husband"]:
            husband = Person.people.get(person["husband"])
            if husband:
                person0.husband = husband
                husband.wife = person0

    return people_list
