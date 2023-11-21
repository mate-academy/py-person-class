class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    new_people_list = [Person(person["name"], person["age"])
                       for person in people_list]

    for person in people_list:
        if "husband" in person and person["husband"]:
            if person["name"] in Person.people:
                husband = Person.people[person["husband"]]
                wife = Person.people[person["name"]]
                wife.husband = husband

        elif "wife" in person and person["wife"]:
            if person["name"] in Person.people:
                wife = Person.people[person["wife"]]
                husband = Person.people[person["name"]]
                husband.wife = wife
    return new_people_list
