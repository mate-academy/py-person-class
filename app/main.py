class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    # Tworzymy wszystkie osoby
    for person in people:
        Person(person.get("name"), person.get("age"))
    result_list = []
    for person in people:
        person_instance = Person.people.get(person.get("name"))
        wife_name = person.get("wife")
        husband_name = person.get("husband")
        if wife_name is not None:
            setattr(person_instance, "wife", Person.people.get(wife_name))
        if husband_name is not None:
            setattr(person_instance, "husband",
                    Person.people.get(husband_name))
        result_list.append(person_instance)
    return result_list
