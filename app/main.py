class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({name: self})


def create_person_list(people: list) -> list:
    main_list = []

    for person in people:
        main_list.append(Person(person["name"], person["age"]))

    for person in people:
        current_person = Person.people[person["name"]]

        if "wife" in person:
            for wife in main_list:
                if person["wife"] == wife.name:
                    current_person.wife = wife

        elif "husband" in person:
            for husband in main_list:
                if person["husband"] == husband.name:
                    current_person.husband = husband

    return main_list
