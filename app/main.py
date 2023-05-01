class Person:
    people = {}

    def __init__(self, name: str, age: int) -> dict:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: "Person") -> "Person":
    person_list = []
    for smb in people:
        name, age = smb["name"], smb["age"]
        person = Person(name, age)
        person_list.append(person)

    for smb in people:
        if smb.get("wife") is not None:
            wife_name = smb["wife"]
            wife = Person.people[wife_name]
            person = Person.people[smb["name"]]
            if wife is not None:
                person.wife = wife
                wife.husband = person
        elif smb.get("husband") is not None:
            husband_name = smb["husband"]
            husband = Person.people[husband_name]
            person = Person.people[smb["name"]]
            if husband is not None:
                person.husband = husband
                husband.wife = person

    return person_list
