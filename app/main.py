class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result_list = [Person(person.get("name"), person.get("age"))
                   for person in people]
    for person in people:
        name = person.get("name")
        wife_name = person.get("wife")
        husband_name = person.get("husband")
        need_person = find_person(result_list, name)
        if wife_name is not None:
            need_person.wife = Person.people[wife_name]
        elif husband_name is not None:
            need_person.husband = Person.people[husband_name]
    return result_list


def find_person(persons: list[Person], name: str) -> (Person, None):
    for person in persons:
        if person.name == name:
            return person
    return None
