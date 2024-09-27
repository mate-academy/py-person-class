class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        new_person = Person(person.get("name"), person.get("age"))
        if (person.get("wife")
                and (p_wife := Person.people.get(person.get("wife")))):
            weddings(new_person, p_wife)
        if (person.get("husband")
                and (p_husband := Person.people.get(person.get("husband")))):
            weddings(p_husband, new_person)
        person_list.append(new_person)
    return person_list


def weddings(person1: Person, person2: Person) -> None:
    person1.wife = person2
    person2.husband = person1
