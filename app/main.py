class Person:
    # Dicionário de classe para armazenar todas as instâncias por nome
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        # Inicializa atributos opcionais
        self.wife = None
        self.husband = None
        # Adiciona a instância ao dicionário da classe
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # Primeira passagem: criar todas as instâncias
    person_list = [Person(p["name"], p["age"]) for p in people]

    # Segunda passagem: resolver relacionamentos (wife/husband)
    for p_dict in people:
        person = Person.people[p_dict["name"]]
        if "wife" in p_dict and p_dict["wife"]:
            person.wife = Person.people.get(p_dict["wife"])
        if "husband" in p_dict and p_dict["husband"]:
            person.husband = Person.people.get(p_dict["husband"])
            
    return person_list
