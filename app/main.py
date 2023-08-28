class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = []
    for human in people:
        name = human["name"]
        age = human["age"]
        person = Person(name, age)

        if human.get("wife"):
            wife_name = human["wife"]
            wife = Person.people.get(wife_name)
            if wife:
                person.wife = wife
                wife.husband = person

        if human.get("husband"):
            husband_name = human["husband"]
            husband = Person.people.get(husband_name)
            if husband:
                person.husband = husband
                husband.wife = person
        persons.append(person)

    return persons
