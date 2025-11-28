class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    people = "name"
def create_person_list(people: list) -> list:
    Person.people = {}
    result = []
    for person_dict in people:
        person_obj = Person(person_dict['name'], person_dict['age'])
        result.append(person_obj)
    for person_dict, person_obj in zip(people, result):
        wife_name = person_dict.get('wife')
        if wife_name:
            person_obj.wife = Person.people[wife_name]
        husband_name = person_dict.get('husband')
        if husband_name:
            person_obj.husband = Person.people[husband_name]
    return result