class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({name: self})


def create_person_list(peoples: list) -> list:
    main_list = []

    for one_people in peoples:
        person = Person(one_people["name"], one_people["age"])
        main_list.append(person)

    for one_people in peoples:
        person = [p for p in main_list if p.name == one_people["name"]][0]

        if "wife" in one_people:
            for wife in main_list:
                if one_people["wife"] == wife.name:
                    person.wife = wife

        elif "husband" in one_people:
            for husband in main_list:
                if one_people["husband"] == husband.name:
                    person.husband = husband

    return main_list
