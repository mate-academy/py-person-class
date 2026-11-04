class Person:
    # Atributo de classe para mapear instancias pelos nomes
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # Adiciona a propria instancia ao dicionario da classe
        Person.people[name] = self


def create_person_list(people_list: list[dict]) -> list[Person]:
    # Limpa o registro da classe para isolar execucoes de testes
    Person.people.clear()

    result_instances: list[Person] = []

    # Passo 1: Instanciar todos os objetos basicos
    for person_dict in people_list:
        new_person = Person(
            name=person_dict["name"],
            age=person_dict["age"]
        )
        result_instances.append(new_person)

    # Passo 2: Conectar as referencias de relacionamento (wife/husband)
    for person_dict in people_list:
        current_name = person_dict["name"]
        current_instance = Person.people[current_name]

        # Processamento para a chave "wife"
        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            current_instance.wife = Person.people[wife_name]

        # Processamento para a chave "husband"
        if "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            current_instance.husband = Person.people[husband_name]

    return result_instances
