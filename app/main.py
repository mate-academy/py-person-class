class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    for human in people:
        Person(name=human["name"], age=human["age"])
    for human in people:
        human_name = human["name"]
        human_wife = human.get("wife", None)
        human_husband = human.get("husband", None)
        if human_wife:
            Person.people[human_name].wife = Person.people[human_wife]
        if human_husband:
            Person.people[human_name].husband = \
                Person.people[human_husband]
    return [*Person.people.values()]
