class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: dict) -> None:
    person_list = []
    for human in people:
        name = human["name"]
        age = human["age"]
        person = Person(name, age)

        person_list.append(person)

    for human in people:
        if human.get("wife"):
            human_name = human.get("name")
            spouse_name = human.get("wife")
            Person.people[human_name].wife = Person.people[spouse_name]

        if human.get("husband"):
            human_name = human.get("name")
            spouse_name = human.get("husband")
            Person.people[human_name].husband = Person.people[spouse_name]

    return person_list
