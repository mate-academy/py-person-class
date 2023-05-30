class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = []
    for person in people:
        new_person = Person(person["name"], person["age"])

        spouse_key = "wife" if "wife" in person else "husband"
        spouse_name = person.get(spouse_key)
        spouse = Person.people.get(spouse_name)

        if spouse and spouse_key == "wife":
            new_person.wife = spouse
            spouse.husband = new_person
        elif spouse and spouse_key == "husband":
            new_person.husband = spouse
            spouse.wife = new_person

        persons.append(new_person)

    return persons
