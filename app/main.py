class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    result = []
    for person in people:
        name = person.get("name")
        age = person.get("age")

        new_person = Person(name, age)

        wife_name = person.get("wife")
        husband_name = person.get("husband")

        if wife_name and wife_name in Person.people:
            new_person.wife = Person.people[wife_name]
            new_person.wife.husband = Person.people[name]
        elif husband_name and husband_name in Person.people:
            new_person.husband = Person.people[husband_name]
            new_person.husband.wife = Person.people[name]

        result.append(new_person)
    return result
