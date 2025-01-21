class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_persons = []

    for persons_data in people:
        name = persons_data["name"]
        age = persons_data["age"]
        person = Person(name, age)
        list_of_persons.append(person)
    i = 0
    for persons_data in people:
        if "wife" in persons_data and persons_data["wife"] is not None:
            wife_name = persons_data["wife"]
            if wife_name in Person.people:
                list_of_persons[i].wife = Person.people[wife_name]
        else:
            delattr(list_of_persons[i], "wife")
        if "husband" in persons_data and persons_data["husband"] is not None:
            husband_name = persons_data["husband"]
            if husband_name in Person.people:
                list_of_persons[i].husband = Person.people[husband_name]
        i += 1

    return list_of_persons
