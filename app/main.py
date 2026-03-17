class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [Person(p["name"], p["age"]) for p in people]
    for i in range(len(people)):
        person_data = people[i]
        person_obj = result[i]
        wife_name = person_data.get("wife")
        if wife_name:
            person_obj.wife = Person.people[wife_name]
        husband_name = person_data.get("husband")
        if husband_name:
            person_obj.husband = Person.people[husband_name]
    return result
