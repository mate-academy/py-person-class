class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    persons = []
    for person_data in people_list:
        name = person_data["name"]
        age = person_data["age"]

        person = Person(name, age)
        Person.people[name] = person

        if person_data.get("wife"):
            wife_name = person_data["wife"]
            if wife_name in Person.people:
                person.wife = Person.people[wife_name]
                person.wife.husband = person

        if person_data.get("husband"):
            husband_name = person_data["husband"]
            if husband_name in Person.people:
                person.husband = Person.people[husband_name]
                person.husband.wife = person

        persons.append(person)
    return persons
