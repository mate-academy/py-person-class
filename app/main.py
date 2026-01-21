class Person:
    people = {}

    def __init__(self, name: str = "", age: int = 0) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    couples = []  # List of tuples (husband name, wife name)

    for person in people:
        person_name = person["name"]
        Person(person_name, person["age"])

        if "wife" in person and person["wife"]:
            couples.append((person_name, person["wife"]))

    people_dict = Person.people
    for husband, wife in couples:
        people_dict[husband].wife = people_dict[wife]
        people_dict[wife].husband = people_dict[husband]

    return [person for person in people_dict.values()]
