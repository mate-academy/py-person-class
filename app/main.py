class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    for person_dict in people:
        name = person_dict.get("name")
        age = person_dict.get("age")
        create_instance = Person(name, age)
        Person.people[name] = create_instance

    for person_dict2 in people:
        if person_dict2.get("wife"):
            name_wife = person_dict2["wife"]
            Person.people[person_dict2["name"]].wife = Person.people[name_wife]

        if person_dict2.get("husband"):
            name_husband = person_dict2["husband"]
            Person.people[person_dict2["name"]].husband = (
                Person.people)[name_husband]
    return list(Person.people.values())
