class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        person_list.append(person)

    for person_data in people:
        person_instance = Person.people[person_data["name"]]

        wife_name = person_data.get("wife")
        if wife_name and wife_name in Person.people:
            person_instance.wife = Person.people[wife_name]

        husband_name = person_data.get("husband")
        if husband_name and husband_name in Person.people:
            person_instance.husband = Person.people[husband_name]

    return person_list
