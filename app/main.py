class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for dict_people in people:
        result.append(Person(dict_people["name"], dict_people["age"]))
    for dict_people2 in people:
        if dict_people2.get("wife") is not None:
            Person.people[dict_people2.get("name")].wife = \
                Person.people[dict_people2.get("wife")]
        if dict_people2.get("husband") is not None:
            Person.people[dict_people2.get("name")].husband = \
                Person.people[dict_people2.get("husband")]
    return result
