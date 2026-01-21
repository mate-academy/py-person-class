class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:

    result_list = []

    for person_data in people:
        name, age, wife_name, husband_name = (
            person_data["name"],
            person_data["age"],
            person_data.get("wife"),
            person_data.get("husband")
        )

        person = Person(name=name, age=age)
        result_list.append(person)

        if wife_name:
            person.wife = Person.people.get(wife_name)
            if person.wife:
                person.wife.husband = person

        elif husband_name:
            person.husband = Person.people.get(husband_name)
            if person.husband:
                person.husband.wife = person

    return result_list
