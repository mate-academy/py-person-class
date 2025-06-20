class Person:
    people: dict["Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def cancel_marriage(self) -> None:
        if self.__dict__.get("wife"):
            self.wife.husband = None
            self.wife = None

        if self.__dict__.get("husband"):
            self.husband.wife = None
            self.husband = None

    def get_married(self, partner_name: str, partner_type: str) -> bool:
        if partner_name not in Person.people or partner_name == self.name:
            return False

        partner: Person = Person.people[partner_name]
        self.cancel_marriage()
        partner.cancel_marriage()

        if partner_type == "husband":
            self.husband = partner
            partner.wife = self
            return True
        elif partner_type == "wife":
            self.wife = partner
            partner.husband = self
            return True

        return False


def create_person_list(people: list) -> list[Person]:
    ans = []
    for person in people:
        ans.append(Person(person["name"], person["age"]))
        if person.get("wife"):
            ans[-1].get_married(person["wife"], "wife")
        elif person.get("husband"):
            ans[-1].get_married(person["husband"], "husband")

    return ans
