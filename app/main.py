class Person:
    people = {}

    def __init__(self, name: object, age: object) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    name_to_person = {}
    persone_list = []

    for person in people:
        new_person = Person(name=person["name"], age=person["age"])
        name_to_person[new_person.name] = new_person
        persone_list.append(new_person)

    for persone in people:
        person_name = persone["name"]
        person = name_to_person.get(person_name)

        if person:
            wife_name = persone.get("wife")
            husband_name = persone.get("husband")

            if wife_name and wife_name in name_to_person:
                person.wife = name_to_person[wife_name]

            if husband_name and husband_name in name_to_person:
                person.husband = name_to_person[husband_name]

    return persone_list
