class Person:

    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_persons = [Person(person_data["name"], person_data["age"])
                       for person_data in people]

    for person_data in people:
        person_instance = Person.people[person_data["name"]]

        if wife_name := person_data.get("wife"):
            person_instance.wife = Person.people[wife_name]

        elif husband_name := person_data.get("husband"):
            person_instance.husband = Person.people[husband_name]

    return list_of_persons
