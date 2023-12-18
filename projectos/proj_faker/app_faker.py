import faker

faker = faker.Faker("zh_CN")

registos = []

for i in range(1, 51):
    id = i
    nome = faker.name()
    email = faker.email()

    registo = {
        "id": id,
        "nome": nome,
        "email": email
    }

    registos.append(registo)

for registo in registos:
    print(registo)