class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    person_dict = {}
    for person in people:
        name = person["name"]
        age = person["age"]
        person_dict[name] = Person(name, age)

    for person in people:
        name = person["name"]
        wife = person.get("wife")
        husband = person.get("husband")
        if wife is not None and name in person_dict:
            person_dict[name].wife = person_dict[wife]
            person_dict[wife].husband = person_dict[name]
        if husband is not None and name in person_dict:
            person_dict[name].husband = person_dict[husband]
            person_dict[husband].wife = person_dict[name]

    return list(person_dict.values())
