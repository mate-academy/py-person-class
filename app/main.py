class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result_list = [
        Person(
            name=person.get("name"),
            age=person.get("age"))
        for person in people]
    for person in people:
        if person.get("wife") is not None:
            husband_name = person.get("name")
            husband = Person.people.get(husband_name)
            wife_name = person.get("wife")
            wife = Person.people.get(wife_name)
            husband.wife = wife
        elif person.get("husband") is not None:
            wife_name = person.get("name")
            wife = Person.people.get(wife_name)
            husband_name = person.get("husband")
            husband = Person.people.get(husband_name)
            wife.husband = husband
    return result_list
