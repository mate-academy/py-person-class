class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    for item in people:
        Person(item["name"], item["age"])

    person_list = []
    for item in people:
        new_person = Person.people.get(item["name"])
        wife_name = item.get("wife")
        husband_name = item.get("husband")
        if wife_name:
            setattr(new_person, "wife", Person.people.get(wife_name))

        if husband_name:
            setattr(new_person, "husband", Person.people.get(husband_name))
        person_list.append(new_person)
    return person_list
