class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list:
    person_list = []
    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        person = Person(name, age)
        person_list.append(person)
    for person_dict in people:
        name = person_dict["name"]
        person = Person.people[name]

        wife_name = person_dict.get("wife")
        if wife_name and wife_name in Person.people:
            person.wife = Person.people[person_dict["wife"]]
        husband_name = person_dict.get("husband")
        if husband_name and husband_name in Person.people:
            person.husband = Person.people[person_dict["husband"]]

    return person_list
