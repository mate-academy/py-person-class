class Person:
    # Atributo de classe para mapear as instancias pelos nomes
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # Adiciona a própria instancia ao dicionário da classe
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    # Limpa o registro da classe para isolar execuções de testes
    Person.people.clear()

    # Passo 1: Instanciar todos os objetos usando List Comprehension
    result_instances = [
        Person(name=p["name"], age=p["age"]) for p in people_list
    ]

    # Passo 2: Conectar as referências de relacionamento (wife/husband)
    for person_dict in people_list:
        current_name = person_dict["name"]
        current_instance = Person.people[current_name]

        # Processamento para a chave "wife" usando dict.get()
        if person_dict.get("wife"):
            wife_name = person_dict["wife"]
            current_instance.wife = Person.people[wife_name]

        # Processamento para a chave "husband" usando dict.get()
        if person_dict.get("husband"):
            husband_name = person_dict["husband"]
            current_instance.husband = Person.people[husband_name]

    return result_instances
