class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    Person.people = {}

    for person_info in people_list:
        Person(person_info["name"], person_info["age"])

    for person_info in people_list:
        person = Person.people[person_info["name"]]

        if "wife" in person_info:
            wife_name = person_info["wife"]
            if wife_name in Person.people:
                person.wife = Person.people[wife_name]
                person.wife.husband = person

        elif "husband" in person_info:
            husband_name = person_info["husband"]
            if husband_name in Person.people:
                person.husband = Person.people[husband_name]
                person.husband.wife = person

    return list(Person.people.values())
