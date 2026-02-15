class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons_list = [Person(entry["name"], entry["age"]) for entry in people]
    for index, person_data in enumerate(people):
        wife_name = person_data.get("wife")
        husband_name = person_data.get("husband")
        if wife_name:
            persons_list[index].wife = Person.people[wife_name]
        if husband_name:
            persons_list[index].husband = Person.people[husband_name]
    return persons_list
