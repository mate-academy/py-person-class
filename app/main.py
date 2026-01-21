class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    pass


def create_person_list(people: list) -> list:
    def find_and_assign_spouse(man: dict, spouse_type: str) -> bool:
        if spouse_type in man and not man[spouse_type] is None:
            person = Person.people[man["name"]]
            setattr(person, spouse_type, Person.people[man[spouse_type]])
            return True
        return False

    for man in people:
        person = Person(man["name"], man["age"])
        Person.people[person.name] = person
    for man in people:
        if not find_and_assign_spouse(man, "wife"):
            find_and_assign_spouse(man, "husband")
    return list(Person.people.values())
