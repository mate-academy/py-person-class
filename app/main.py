class Person:

    people = {}

    def __init__(
            self,
            name: str,
            age: str
    ) -> None:
        self.name = name
        self.age = age
        self.people[name] = self

    def set_spouse(
            self,
            spouse_type: str,
            spouse_name: str
    ) -> None:
        switcher = {"wife": "husband", "husband": "wife"}
        if spouse_name and self.people.get(spouse_name):
            setattr(self, spouse_type, self.people[spouse_name])
            setattr(self.people[spouse_name], switcher[spouse_type], self)


def create_person_list(people: list) -> list:
    result = []
    for human in people:
        person = Person(human["name"], human["age"])
        if human.get("husband"):
            person.set_spouse("husband", human["husband"])
        if human.get("wife"):
            person.set_spouse("wife", human["wife"])
        result.append(person)
    return result
