class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = []

    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])
        people_list.append(person)

    for person_dict in people:
        name = person_dict["name"]
        person = Person.people[name]

        wife_name = person_dict.get("wife")
        if wife_name:
            person.wife = Person.people[wife_name]

        husband_name = person_dict.get("husband")
        if husband_name:
            person.husband = Person.people[husband_name]
    return people_list
