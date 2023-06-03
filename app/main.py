class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    list_of_persons = []
    for person in people:
        name = person["name"]
        age = person["age"]
        new_person = Person(name=name, age=age)
        if "husband" in person and person["husband"] is not None:
            new_person.husband = person["husband"]
        elif "wife" in person and person["wife"] is not None:
            new_person.wife = person["wife"]
        list_of_persons.append(new_person)
    for existed_person in list_of_persons:
        if "husband" in existed_person.__dir__():
            existed_person.husband = Person.people.get(existed_person.husband)
        elif "wife" in existed_person.__dir__():
            existed_person.wife = Person.people.get(existed_person.wife)
    return list_of_persons
