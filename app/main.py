class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_info in people:
        age = person_info["age"]
        name = person_info["name"]
        person = Person(name, age)

        if "husband" in person_info:
            husband_name = person_info["husband"]
            if husband_name in Person.people:
                person.husband = Person.people[husband_name]
                Person.people[husband_name].wife = person
        if "wife" in person_info:
            wife_name = person_info["wife"]
            if wife_name in Person.people:
                person.wife = Person.people[wife_name]
                Person.people[wife_name].husband = person
        person_list.append(person)
    return person_list
