class Person:

    people = {}

    def __init__(self, name: int, age: str) -> None:
        self.name = name
        self.age = age
        self.spouse = None
        Person.people[name] = self

    def set_spouse(self, spouse_name: int) -> None:
        if spouse_name in Person.people:
            self.spouse = Person[spouse_name]
            Person.people[spouse_name].spouse = self

    def create_person_list(self, people: list) -> list:
        person_instances = []

        for person_info in people:
            name = person_info["name"]
            age = person_info["age"]
            person = Person(name, age)
            spouse_name = person_info.get("wife") or person_info.get("husband")
            if spouse_name:
                person.set_spouse(spouse_name)
            person_instances.append(person)
        return person_instances
