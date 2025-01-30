from random import randint
from faker import Faker

def rand_ratio():
    return randint(840, 900), randint(473, 573)
fake = Faker('pt_BR')
# print(signature(fake.random_number))
def make_recipe():
    return {
        'id':fake.random_number(digits=2, fix_len=True),
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos',
        'servings': fake.random_number(digits=2, fix_len=True),
        'servings_unit': 'Porção',
        'preparation_steps': fake.text(3000),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': fake.word()
        },
        'cover': {
            'url': 'https://img.freepik.com/fotos-gratis/as-maos-do-chef-cortando-vegetais-em-sua-cozinha_155003-42433.jpg?t=st=1738179938~exp=1738183538~hmac=4bbe76718badfd2f529e60d4122b6392f7e16fe718e2199a84040ebad92b0243&w=1380',
        }
    }
if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())