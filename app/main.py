class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    list_of_instances = []

    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        new_person = Person(name, age)

        wife_name = person_data.get("wife")
        husband_name = person_data.get("husband")

        if wife_name and wife_name in Person.people:
            new_person.wife = Person.people[wife_name]
            Person.people[wife_name].husband = new_person

        if husband_name and husband_name in Person.people:
            new_person.husband = Person.people[husband_name]
            Person.people[husband_name].wife = new_person

        list_of_instances.append(new_person)

    return list_of_instances
