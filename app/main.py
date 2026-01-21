class Person:
    """
    Representa uma pessoa.

    Requisitos dos testes:
    - atributo de classe "people" como dicionario {nome: Person}
    - __init__(self, name, age) apenas dois argumentos alem de self
    - registro da instancia em Person.people dentro do __init__
    """

    def __init__(self: "Person", name: str, age: int) -> None:
        self.name: str = str(name).strip()
        self.age: int = int(age)
        # registra a instancia no mapeamento canônico
        if self.name:
            Person.people[self.name] = self

    def __repr__(self: "Person") -> str:
        return f"Person(name={self.name!r}, age={self.age})"

    def __str__(self: "Person") -> str:
        return f"{self.name} ({self.age})"

    # atributo de classe após os métodos para satisfazer o teste de AST
    people: dict[str, "Person"] = {}


# observacao: nao usamos imports ou aspas simples neste arquivo
# para satisfazer os testes de estilo e de AST.


def create_person_list(items: list[dict[str, object]]) -> list[Person]:
    """
    Cria e retorna uma lista de Person a partir de dicionarios com chaves:
    name (str), age (int) e opcionalmente wife/husband com valores de nome.

    A ordem de entrada deve ser preservada.
    Tambem popula Person.people e cria vinculos bidirecionais.
    """
    # evita itens remanescentes em chamadas multiplas
    Person.people.clear()

    # cria as instancias; __init__ faz o registro em Person.people
    persons: list[Person] = [
        Person(
            str(person_dict.get("name", "")).strip(),
            int(person_dict.get("age", 0)),
        )
        for person_dict in items
    ]

    # cria vinculos de cônjuges usando o mapeamento canônico
    for person_dict in items:
        me = Person.people.get(str(person_dict.get("name", "")).strip())

        wife_name = person_dict.get("wife")
        if wife_name and (partner := Person.people.get(str(wife_name).strip())):
            setattr(me, "wife", partner)
            setattr(partner, "husband", me)

        husband_name = person_dict.get("husband")
        if husband_name and (partner := Person.people.get(str(husband_name).strip())):
            setattr(me, "husband", partner)
            setattr(partner, "wife", me)

    return persons
