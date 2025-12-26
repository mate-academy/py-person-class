class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        current_person = Person.people.get(person["name"])
        wife_name = person.get("wife")
        husband_name = person.get("husband")

        if wife_name:
            spouse = Person.people.get(wife_name)
            if spouse:
                current_person.wife = spouse
                spouse.husband = current_person

        if husband_name:
            spouse = Person.people.get(husband_name)
            if spouse:
                current_person.husband = spouse
                spouse.wife = current_person

    return person_list
