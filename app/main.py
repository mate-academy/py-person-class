class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person_list.append(Person(name, age))

    for person_data in people:
        if "wife" in person_data:
            spouse_key = "wife"
        elif "husband" in person_data:
            spouse_key = "husband"

        current_person = Person.people.get(person_data["name"])
        spouse_person = Person.people.get(person_data.get(spouse_key))

        if current_person is not None and spouse_person is not None:
            if spouse_key == "wife":
                current_person.wife = spouse_person
            elif spouse_key == "husband":
                current_person.husband = spouse_person

    return person_list
