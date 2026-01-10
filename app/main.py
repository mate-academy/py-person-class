class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

def create_person_list(people: list) -> list:
    first_list = [Person(person["name"], person["age"]) for person in people]

    for index, person in enumerate(people):
        wife_name = person.get("wife")
        if wife_name:
            setattr(first_list[index], "wife", Person.people[wife_name])
        husband_name = person.get("husband")
        if husband_name:
            setattr(first_list[index], "husband", Person.people[husband_name])

    return first_list
