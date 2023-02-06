class Person:
    people = {}

    def __init__(self, name: str, age: int, **kwargs) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    list_with_instances = [Person(**person) for person in people]
    for person in people:
        wife_name = person.get("wife")
        husband_name = person.get("husband")
        if wife_name:
            Person.people[
                person.get("name")
            ].wife = Person.people[wife_name]
        elif husband_name:
            Person.people[
                person.get("name")
            ].husband = Person.people[husband_name]

    return list_with_instances
