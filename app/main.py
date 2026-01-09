class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    person_list = [Person(person_dict.get("name"),
                          person_dict.get("age")) for person_dict in people]

    for i in range(len(people)):
        person_dict = people[i]
        person = person_list[i]
        wife_name = person_dict.get("wife")
        husband_name = person_dict.get("husband")

        if wife_name is not None:
            person.wife = Person.people.get(wife_name)
        if husband_name is not None:
            person.husband = Person.people.get(husband_name)

    return person_list
