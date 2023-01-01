class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for human in people:
        person = Person(human["name"], human["age"])
        person_list.append(person)

    for human in people:
        for person in person_list:
            human_is_person = person.name == human["name"]
            has_wife = "wife" in human and human["wife"] is not None
            has_husband = "husband" in human and human["husband"] is not None
            if human_is_person and has_wife:
                person.wife = person.__class__.people[human["wife"]]
            elif human_is_person and has_husband:
                person.husband = person.__class__.people[human["husband"]]

    return person_list
