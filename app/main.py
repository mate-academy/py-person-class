class Person:
    people = {}
    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self
    pass


def create_person_list(people_l: list) -> list:
    person_instances = []
    for person in people_l:
        person_n = Person(person["name"], person["age"])
        person_instances.append(person_n)

    for person in people_l:
        person_name = Person.people[person["name"]]
        if "wife" in person:
            spouse_k = "wife"
        else:
            spouse_k = "husband"
        spouse_name = person.get(spouse_k)
        if spouse_name:
            setattr(person_name, spouse_k, Person.people[spouse_name])

    return person_instances
