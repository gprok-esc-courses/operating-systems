from faker import Faker

fake = Faker()

for i in range(10):
    print(fake.last_name(), fake.first_name(), fake.email(),
       fake.credit_card_number())