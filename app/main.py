class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self


@staticmethod
def create_person_list(people: list) -> list:
    persons = [
        Person(person_dict["name"], person_dict["age"]) 
        for person_dict in people
    ]

    for person_dict in people:
        person = Person.people[person_dict["name"]]
        spouse_key = person_dict.get("wife") or person_dict.get("husband")
        if spouse_key:
            setattr(
                person, "wife" if "wife" in person_dict else "husband",
                Person.people[spouse_key]
    )
    
    return persons
