class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    result = []

    for person_data in people_list:
        name = person_data["name"]
        age = person_data["age"]

        person = Person(name, age)

        if "wife" in person_data and person_data["wife"] is not None:
            spouse_name = person_data["wife"]
            person.wife = Person.people.get(spouse_name)
            if person.wife is not None:
                person.wife.husband = person

        elif "husband" in person_data and person_data["husband"] is not None:
            spouse_name = person_data["husband"]
            person.husband = Person.people.get(spouse_name)
            if person.husband is not None:
                person.husband.wife = person

        result.append(person)

    return result
