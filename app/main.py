class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(data: list) -> list:
    persons = [Person(person["name"], person["age"]) for person in data]
    for i in range(len(data)):
        if "wife" in data[i] and data[i]["wife"] is not None:
            wife = data[i].get("wife")
            if wife in Person.people:
                persons[i].wife = Person.people[wife]
        elif "husband" in data[i] and data[i]["husband"] is not None:
            husband = data[i].get("husband")
            if husband in Person.people:
                persons[i].husband = Person.people[husband]
    return persons
