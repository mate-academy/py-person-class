class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = []
    for person_info in people:
        if person_info["name"] in Person.people:
            person = Person.people[person_info["name"]]
            person.age = person_info["age"]

        else:
            person = Person(person_info["name"], person_info["age"])
        persons.append(person)
        wife = person_info.get("wife")
        husband = person_info.get("husband")
        if wife is not None:
            if wife in Person.people:
                wife = Person.people[wife]
                person.__dict__["wife"] = wife
            else:
                wife = Person(wife, 0)
                person.__dict__["wife"] = wife
            wife.__dict__["husband"] = person
        elif husband is not None:
            if husband in Person.people:
                husband = Person.people[husband]
                person.__dict__["husband"] = husband
            else:
                husband = Person(husband, 0)
                person.__dict__["husband"] = husband
            husband.__dict__["wife"] = person
    return persons
