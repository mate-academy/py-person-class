class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    new_people_list = []
    for person_info in people:
        name = person_info["name"]
        age = person_info["age"]
        person = Person(name, age)
        new_people_list.append(person)

    for person_info in people:
        name = person_info["name"]
        person = Person.people[name]

        if "wife" in person_info and person_info["wife"]:
            wife_name = person_info["wife"]
            person.wife = Person.people[wife_name]

        if "husband" in person_info and person_info["husband"]:
            husband_name = person_info["husband"]
            person.husband = Person.people[husband_name]

    return new_people_list
