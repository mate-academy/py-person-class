class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self

    def remove_spouse_attribute(self):
        if self.wife is None:
            del self.wife
        if self.husband is None:
            del self.husband


def create_person_list(people: list) -> list:
    created_people = []
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        created_people.append(person)

        if "wife" in person_data and person_data["wife"] in Person.people:
            wife_name = person_data["wife"]
            person.wife = Person.people.get(wife_name)
            if person.wife:
                person.wife.husband = person
        elif "husband" in person_data and person_data["husband"] in Person.people:
            husband_name = person_data["husband"]
            person.husband = Person.people.get(husband_name)
            if person.husband:
                person.husband.wife = person

        person.remove_spouse_attribute()

    return created_people
