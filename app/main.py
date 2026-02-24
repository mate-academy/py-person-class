class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    result = [Person(person_dict.get("name"), person_dict.get("age"))
              for person_dict in people]
    for person_dict in people:
        if (person_dict.get("wife") is not None
                and Person.people.get(person_dict.get("wife")) is not None):
            Person.people.get(person_dict.get("name")).wife = (
                Person.people).get(person_dict.get("wife"))
        if (person_dict.get("husband") is not None
                and Person.people.get(person_dict.get("husband")) is not None):
            Person.people.get(person_dict.get("name")).husband = (
                Person.people).get(person_dict.get("husband"))
    return result
