class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people_list: list[dict]) -> list[Person]:

    person_list = [
        Person(person["name"], person["age"])
        for person in people_list
    ]
    for pers in people_list:
        wife_name, husband_name = pers.get("wife"), pers.get("husband")
        current_person = Person.people.get(pers["name"])
        if wife_name:
            current_person.wife = Person.people.get(wife_name)

        if husband_name:
            current_person.husband = \
                Person.people.get(husband_name)

    return person_list
