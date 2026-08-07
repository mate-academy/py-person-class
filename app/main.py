class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = [Person(person_dict["name"],
                      person_dict["age"])
               for person_dict in people]
    for person_dict in people:
        current_person = Person.people[person_dict["name"]]
        if person_dict.get("wife"):
            current_person.wife = Person.people[person_dict.get("wife")]
        elif person_dict.get("husband"):
            current_person.husband = Person.people[person_dict.get("husband")]
    return persons
