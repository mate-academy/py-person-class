class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)

        if "wife" in person_data and person_data["wife"]:
            wife_name = person_data["wife"]
            if wife_name in Person.people:
                person.wife = Person.people[wife_name]
                Person.people[wife_name].husband = person

            elif "husband" in person_data and person_data["husband"]:
                husband_name = person_data["husband"]
                if husband_name in Person.people:
                    person.husband = Person.people[husband_name]
                    Person.people[husband_name].wife = person

        person_list.append(person)

    return person_list
