class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def wife_(self, wife_name: str) -> None:
        if wife_name and wife_name in Person.people:
            self.wife = Person.people[wife_name]

    def husband_(self, husband_name: str) -> None:
        if husband_name and husband_name in Person.people:
            self.husband = Person.people[husband_name]


def create_person_list(people_list: list) -> list:
    for person_dict in people_list:
        Person(person_dict["name"], person_dict["age"])

    for person_dict in people_list:
        person = Person.people[person_dict["name"]]
        wife_name = person_dict.get("wife")
        husband_name = person_dict.get("husband")
        if wife_name:
            person.wife_(wife_name)
        if husband_name:
            person.husband_(husband_name)
    return list(Person.people.values())
