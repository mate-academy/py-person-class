class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_data: list) -> list:
    # Fase 1: Criar todos os objetos e a lista para retorno
    person_instances = []
    for person_dict in people_data:
        new_person = Person(name=person_dict['name'], age=person_dict['age'])
        person_instances.append(new_person)


    for person_dict in people_data:
        # 'elif' corrigido para estar alinhado com 'if'
        if "wife" in person_dict and person_dict["wife"] is not None:
            person_object = Person.people[person_dict['name']]
            wife_object = Person.people[person_dict['wife']]
            person_object.wife = wife_object
        elif "husband" in person_dict and person_dict["husband"] is not None:
            person_object = Person.people[person_dict['name']]
            husband_object = Person.people[person_dict['husband']]
            person_object.husband = husband_object

    return person_instances