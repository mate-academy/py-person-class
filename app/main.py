class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for human in people:
        new_person = Person(human["name"], human["age"])
        if human.get("wife"):
            new_person.wife = human.get("wife")
        elif human.get("husband"):
            new_person.husband = human.get("husband")
        person_list.append(new_person)

    for person in person_list:
        wife = getattr(person, "wife", None)
        husband = getattr(person, "husband", None)

        if wife:
            person.wife = Person.people[wife]

        if husband:
            person.husband = Person.people[husband]

    return person_list
