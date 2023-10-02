class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    instances_list = []

    for person_info in people:
        person = Person(person_info["name"], person_info["age"])

        husband = person_info.get("husband")
        wife = person_info.get("wife")

        if wife:
            person.wife = Person.people.get(wife)
            if person.wife:
                person.wife.husband = person

        if husband:
            person.husband = Person.people.get(husband)
            if person.husband:
                person.husband.wife = person

        instances_list.append(person)
    return instances_list
