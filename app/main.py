class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = []
    for person_data in people:
        person = Person(person_data["name"], person_data["age"])
        people_list.append(person)
    for person_data in people:
        person = Person.people[person_data["name"]]
        wife_name = person_data.get("wife")
        husband_name = person_data.get("husband")

        if wife_name:
            person.wife = Person.people.get(wife_name)
            if person.wife:
                person.wife.husband = person

        if husband_name:
            person.husband = Person.people.get(husband_name)
            if person.husband:
                person.husband.wife = person
    return people_list
