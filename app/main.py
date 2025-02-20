class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = []

    for human in people:
        name = human["name"]
        age = human["age"]

        person = Person(name, age)

        if "wife" in human and human["wife"]:
            wife_name = human["wife"]
            person.wife = Person.people.get(wife_name)
            if person.wife:
                person.wife.husband = person

        if "husband" in human and human["husband"]:
            husband_name = human["husband"]
            person.husband = Person.people.get(husband_name)
            if person.husband:
                person.husband.wife = person

        person_list.append(person)
    return person_list
