class Person:

    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_in: list) -> list:
    result = []
    for human in people_in:
        result.append(Person(human["name"], human["age"]))

    for human in people_in:
        current_person = Person.people.get(human["name"])
        current_wife = human.get("wife")
        if current_wife:
            current_person.wife = Person.people[current_wife]
        current_husband = human.get("husband")
        if current_husband:
            current_person.husband = Person.people[current_husband]
    return result
