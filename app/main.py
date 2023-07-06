class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for one_p in people:
        name, age = one_p["name"], one_p["age"]
        person = Person(name, age)
        person_list.append(person)

    for one_p in people:
        if one_p.get("wife") is not None:
            wife_name = one_p["wife"]
            wife = Person.people[wife_name]
            person = Person.people[one_p["name"]]
            if wife is not None:
                person.wife = wife
                wife.husband = person
        elif one_p.get("husband") is not None:
            husband_name = one_p["husband"]
            husband = Person.people[husband_name]
            person = Person.people[one_p["name"]]
            if husband is not None:
                person.husband = husband
                husband.wife = person
    return person_list
