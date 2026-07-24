class Person:

    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person.get("name"), person.get("age"))
    for person in people:
        person_obj = Person.people[person["name"]]
        if not person_obj:
            continue
        wife_name = person.get("wife")
        if wife_name:
            if Person.people[wife_name]:
                person_obj.wife = Person.people[wife_name]
        else:
            husband_name = person.get("husband")
            if husband_name:
                if Person.people[husband_name]:
                    person_obj.husband = Person.people[husband_name]
    return list(Person.people.values())
