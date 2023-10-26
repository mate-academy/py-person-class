class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for someone in people:
        name = someone["name"]
        age = someone["age"]
        person = Person(name, age)
        person_list.append(person)

    for someone in people:
        if "wife" in someone and someone["wife"] is not None:
            wife_name = someone["wife"]
            for wife in person_list:
                if wife_name == wife.name:
                    for person in person_list:
                        if person.name == someone["name"]:
                            person.wife = wife

    for someone in people:
        if "husband" in someone.keys() and someone["husband"] is not None:
            husband_name = someone["husband"]
            for husband in person_list:
                if husband_name == husband.name:
                    for person in person_list:
                        if person.name == someone["name"]:
                            person.husband = husband

    return person_list
