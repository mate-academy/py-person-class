class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person1["name"], person1["age"]) for person1 in people]

    count = 0
    for person1 in people:
        if "wife" in person1:
            for person2 in person_list:
                if person2.name == person1["wife"]:
                    person_list[count].wife = person2

        else:
            for person2 in person_list:
                if person2.name == person1["husband"]:
                    person_list[count].husband = person2
        count += 1

    return person_list
