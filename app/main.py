class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def find_partner(person: Person, spouse_name: str, is_wife: bool) -> None:
    spouse = Person.people.get(spouse_name)
    if spouse:
        if is_wife:
            person.wife = spouse
            spouse.husband = person
        else:
            person.husband = spouse
            spouse.wife = person


def create_person_list(people: list) -> list:
    created_person_list = [
        Person(persona["name"], persona["age"])
        for persona in people
    ]

    for persona in people:
        person = Person.people.get(persona["name"])
        if person:
            if wife_name := persona.get("wife"): # noqa
                find_partner(person, wife_name, is_wife=True)
            if husband_name := persona.get("husband"): # noqa
                find_partner(person, husband_name, is_wife=False)

    return created_person_list
