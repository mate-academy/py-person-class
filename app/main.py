class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = [Person(person.get("name"), person.get("age"))
                        for person in people]
    for human in people:
        wife = human.get("wife")
        if wife is not None:
            Person.people.get(human.get("name")).wife = (
                Person.people.get(wife))
        husband = human.get("husband")
        if husband is not None:
            Person.people.get(human.get("name")).husband = (
                Person.people.get(husband))
    return person_instances
