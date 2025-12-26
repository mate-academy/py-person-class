class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_answer = []
    for person in people:
        new_person = Person(name=person["name"], age=person["age"])
        wife_name = person.get("wife")
        husband_name = person.get("husband")

        if wife_name is not None:
            new_person.wife = wife_name
        if husband_name is not None:
            new_person.husband = husband_name
        people_answer.append(new_person)

    for person in people_answer:
        if person.wife is not None:
            person.wife = Person.people[person.wife]
        else:
            del person.wife
        if person.husband is not None:
            person.husband = Person.people[person.husband]
        else:
            del person.husband
    return people_answer
