class Person:
    people = {}
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = {p_data["name"]: Person(p_data["name"], p_data["age"]) for p_data in people}
    for p_data in people:
        person = persons[p_data["name"]]
        if "wife" in p_data and p_data["wife"]:
            person.wife = persons[p_data["wife"]]
        if "husband" in p_data and p_data["husband"]:
            person.husband = persons[p_data["husband"]]

    return list(persons.values())
