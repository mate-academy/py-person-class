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

        married_key = "wife" if "wife" in person else "husband"
        married_name = person.get(married_key)
        married = Person.people.get(married_name)

        if married:
            if married_key == "wife":
                new_person.wife = married
                married.husband = new_person
            else:
                new_person.husband = married
                married.wife = new_person

        persons.append(new_person)

    return persons
