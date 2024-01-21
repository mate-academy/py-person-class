class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        main_person = Person.people[person["name"]]
        if "wife" in person and person["wife"]:
            # Setting wife and linking back to husband
            main_person.wife = Person.people[person["wife"]]
            main_person.wife.husband = main_person
        elif "husband" in person and person["husband"]:
            # Setting husband and linking back to wife
            main_person.husband = Person.people[person["husband"]]
            main_person.husband.wife = main_person

    return [Person.people[person["name"]] for person in people]
