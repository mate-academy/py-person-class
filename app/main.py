class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age

        Person.people[name] = self

def create_person_list(people: list) -> list:
    for person_data in people:
        Person(person_data["name"], person_data["age"])

    for person_data in people:
        person = Person.people[person_data["name"]]
        spouse_name = person_data.get("wife") or person_data.get("husband")

        if spouse_name:
            spouse = Person.people.get(spouse_name)

            if spouse:
                if "wife" in person_data:
                    person.wife = spouse
                else:
                    person.husband = spouse

    return list(Person.people.values())
