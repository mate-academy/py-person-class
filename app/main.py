class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:

    new_person_list = []
    for person_list in people:
        new_person_list.append(Person(person_list["name"],
                                      person_list["age"]))

    for person in new_person_list:
        Person.people[person.name] = person

    for person_list in people:
        current_person = None
        for person in new_person_list:
            if person.name == person_list["name"]:
                current_person = person

        wife_name = person_list.get("wife")
        if wife_name is not None:
            for wife in new_person_list:
                if wife.name == wife_name:
                    current_person.wife = wife

        husband_name = person_list.get("husband")
        if husband_name is not None:
            for husband in new_person_list:
                if husband.name == husband_name:
                    current_person.husband = husband

    return new_person_list
