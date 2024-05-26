class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: dict) -> list:
    person_list = []
    for one in people:
        person = Person(one["name"], one["age"])
        person_list.append(person)

    for one in people:
        person = Person.people[one["name"]]
        wife_name = one.get("wife")
        husband_name = one.get("husband")
        if wife_name:
            person.wife = Person.people[wife_name]
            person.wife.husband = person
        elif husband_name:
            person.husband = Person.people[husband_name]
            person.husband.wife = person

    return person_list
