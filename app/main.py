class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        person_list.append(new_person)

    for person in person_list:
        for second_half in people:
            if second_half.get("wife") and second_half["wife"] == person.name:
                for pers in person_list:
                    if pers.name == second_half["name"]:
                        pers.wife = person
                        pers.wife.husband = pers
    return person_list
