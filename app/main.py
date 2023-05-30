class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person_info in people:
        person = Person(person_info["name"], person_info["age"])

        wife_name = person_info.get("wife")
        if wife_name in Person.people:
            person.wife = Person.people[wife_name]
            person.wife.husband = person

        husband_name = person_info.get("husband")
        if husband_name in Person.people:
            person.husband = Person.people[husband_name]
            person.husband.wife = person
        person_list.append(person)

    return person_list
