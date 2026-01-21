class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    for dict_num in people:
        Person(dict_num["name"], dict_num["age"])
    for dict_num in people:
        if dict_num.get("wife") is not None:
            Person.people[dict_num["name"]].wife \
                = Person.people[dict_num["wife"]]
        if dict_num.get("husband") is not None:
            Person.people[dict_num["name"]].husband \
                = Person.people[dict_num["husband"]]
    return [Person.people[dict_num["name"]] for dict_num in people]
