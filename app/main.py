class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    Person.people.clear()
    for person_dict in people:
        Person(person_dict["name"], person_dict["age"])

    for person_dict in people:
        person_instance = Person.people[person_dict["name"]]

        spouse_name = person_dict.get('wife')
        if spouse_name:
            person_instance.wife = Person.people[person_dict["wife"]]

        spouse_name = person_dict.get('husband')
        if spouse_name:
            person_instance.husband = Person.people[person_dict["husband"]]
    for person_dict in people:
        person_list.append(Person.people[person_dict["name"]])
    return person_list
