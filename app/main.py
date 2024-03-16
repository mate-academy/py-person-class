class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self] = self


def create_person_list(people: list) -> list:
    people_by_name = []
    for person in people:
        person_by_name = Person(person["name"], person["age"])
        if person.get("wife"):
            person_by_name.wife = person["wife"]
        if person.get("husband"):
            person_by_name.husband = person["husband"]

        people_by_name.append(person_by_name)

    for person in people_by_name:
        for partner in people_by_name:
            if ("wife" in dir(person)) and person.wife == partner.name:
                person.wife = partner
            if ("husband" in dir(person)) and person.husband == partner.name:
                person.husband = partner

    return people_by_name


# people = [
#     {"name": "Ross", "age": 30, "wife": "Rachel"},
#     {"name": "Joey", "age": 29, "wife": None},
#     {"name": "Rachel", "age": 28, "husband": "Ross"}
# ]
#
#
# person_list = create_person_list(people)
