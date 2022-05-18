class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    new_people_list = []
    people_with_partner = []
    for person_dict in people:
        person = Person(person_dict['name'], person_dict['age'])

        if 'wife' in person_dict.keys():
            if person_dict['wife']:
                person.partner = person_dict['wife']
                person.wife = person.partner
                people_with_partner.append(person)

        elif 'husband' in person_dict.keys():
            if person_dict['husband']:
                person.partner = person_dict['husband']
                person.husband = person.partner
                people_with_partner.append(person)
        new_people_list.append(person)

    for person1 in people_with_partner:
        person2 = person1.people[person1.partner]
        if 'wife' in person1.__dict__:
            person1.wife = person2
        elif 'husband' in person1.__dict__:
            person1.husband = person2
    return new_people_list
