class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for i in range(len(people)):
        for person_obj, person_data in zip(person_list, people):
            if wife_name := person_data.get("wife"):
                person_obj.wife = Person.people[wife_name]
            elif husband_name := person_data.get("husband"):
                person_obj.husband = Person.people[husband_name]
    return person_list
