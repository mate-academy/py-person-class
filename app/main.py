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
        name = someone["name"]
        person = Person.people[name]
        if "wife" in someone and someone["wife"]:
            wife_name = someone["wife"]
            person.wife = Person.people[wife_name]

        if "husband" in someone and someone["husband"]:
            husband_name = someone["husband"]
            person.husband = Person.people[husband_name]

    return person_list
