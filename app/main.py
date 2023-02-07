class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    person_list = []
    for human in people_list:
        person = Person(human["name"], human["age"])
        spouse = human.get("wife") or human.get("husband")
        if spouse in Person.people:
            spouse_link = Person.people[spouse]
            if "wife" in human:
                person.wife = spouse_link
                spouse_link.husband = person
            else:
                person.husband = spouse_link
                spouse_link.wife = person
        person_list.append(person)
    return person_list
