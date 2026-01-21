class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self
    pass


def create_person_list(people: list) -> list:
    person_list = [Person(p.get("name"), p.get("age")) for p in people]

    for p_obj, p_dict in zip(person_list, people):
        wife = p_dict.get("wife")
        husband = p_dict.get("husband")
        if wife:
            p_obj.wife = wife
        elif husband:
            p_obj.husband = husband

    return person_list
