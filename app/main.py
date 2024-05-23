class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_people = [Person(person_data["name"], person_data["age"])
                      for person_data in people]

    for person_data in people:
        name = person_data["name"]
        person = Person.people[name]

        if "wife" in person_data:
            wife_name = person_data.get("wife")
            if wife_name:
                spouse = Person.people[wife_name]
                person.wife = spouse

        if "husband" in person_data:
            husband_name = person_data.get("husband")
            if husband_name:
                spouse = Person.people[husband_name]
                person.husband = spouse
    return list_of_people
