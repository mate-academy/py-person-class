class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    people_list = [(Person(value["name"], value["age"]))
                   for i, value in enumerate(people)]
    for person in people:
        wife_name = person.get("wife")
        husband = person.get("husband")
        current_person = Person.people[person["name"]]
        if wife_name:
            current_person.wife = Person.people[wife_name]
        if husband:
            current_person.husband = Person.people[husband]
    return people_list
