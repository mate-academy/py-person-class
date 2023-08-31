class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({name: self})


def create_person_list(peoples: list) -> list:
    main_list = []

    for people in peoples:
        person = Person(people["name"], people["age"])
        main_list.append(person)

    for people in peoples:
        person = [p for p in main_list if p.name == people["name"]][0]

        if "wife" in people:
            for wife in main_list:
                if people["wife"] == wife.name:
                    person.wife = wife

        elif "husband" in people:
            for husband in main_list:
                if people["husband"] == husband.name:
                    person.husband = husband

    return main_list

