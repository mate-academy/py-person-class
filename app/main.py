class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        person_list.append(person)

    for person_data in people:
        person = Person.people[person_data["name"]]
        if person_data.get("wife") is not None:
            wife_name = person_data["wife"]
            person.wife = Person.people[wife_name]
            Person.people[wife_name].husband = person
        if person_data.get("husband") is not None:
            husband_name = person_data["husband"]
            person.husband = Person.people[husband_name]
            Person.people[husband_name].wife = person

    return person_list
