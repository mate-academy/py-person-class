class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self

    def wife_add(self, id):
        self.wife = id

    def husband_add(self, id):
        self.husband = id


def create_person_list(people_list: list) -> list:
    people = []
    people.extend(people_list)
    for index in range(len(people)):
        people[index] = Person(people[index]['name'], people[index]['age'])

    for person in range(len(people_list)):
        married_gender = 'wife' if 'wife' in people_list[person] else 'husband'
        for married_with in range(len(people_list)):
            if people_list[person][married_gender] == \
                    people_list[married_with]['name'] \
                    and married_gender == 'wife':
                people[person].wife_add(people[married_with])
            if people_list[person][married_gender] == \
                    people_list[married_with]['name'] \
                    and married_gender == 'husband':
                people[person].husband_add(people[married_with])

    return people
