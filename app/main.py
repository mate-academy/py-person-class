class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: dict) -> list:
    for per in people:
        Person(per["name"], per["age"])

    for per in people:
        person = Person.people[per["name"]]
        spouse_name = per.get("wife") or per.get("husband")
        if spouse_name:
            spouse = Person.people[spouse_name]
            if "wife" in per:
                person.wife = spouse
            else:
                person.husband = spouse
            person.spouse = spouse

    return list(Person.people.values())
