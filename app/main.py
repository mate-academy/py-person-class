class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    [Person(person_dict["name"], person_dict["age"]) for person_dict in people]

    for person_dict in people:
        person = Person.people[person_dict["name"]]

        wife_name = person_dict.get("wife")
        husband_name = person_dict.get("husband")

        if wife_name and not getattr(person, "wife", None):
            person.wife = Person.people[wife_name]
            if not getattr(person.wife, "husband", None):
                person.wife.husband = person

        if husband_name and not getattr(person, "husband", None):
            person.husband = Person.people[husband_name]
            if not getattr(person.husband, "wife", None):
                person.husband.wife = person

    return list(Person.people.values())
