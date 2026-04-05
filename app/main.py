class Person:
    people = {}
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

def create_person_list(people: list) -> list:
    result = []
    Person.people.clear()

    for item in people:
        person_obj = Person(name=item["name"], age=item["age"])
        result.append(person_obj)

    for person_dict in people:
        person = Person.people[person_dict["name"]]
        for key in ("wife", "husband"):
            partner_name = person_dict.get(key)
            if partner_name is not None:
                setattr(person, key, Person.people[partner_name])
    return result
