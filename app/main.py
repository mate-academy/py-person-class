class Person:
    people = {}
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self

def create_person_list(people: list[dict]) -> list[Person]:
    person_list = [Person(person_dict.get("name"), person_dict.get("age")) for person_dict in people]
    for person_dict2 in people:
        if person_dict2.get("wife") != None:
            Person.people[person_dict2.get("name")].wife = Person.people[person_dict2.get("wife")]
        elif person_dict2.get("husband") != None:
            Person.people[person_dict2.get("name")].husband = Person.people[person_dict2.get("husband")]
        else:
            pass
    return person_list
