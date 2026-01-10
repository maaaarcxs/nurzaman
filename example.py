from accounts.models import User
from django.db import models

# 1. Создать базу данных
# CREATE DATABASE shop_db;

# 2. Удалить базу данных
# DROP DATABASE shop_db;

# 3. Создать таблицу
# CREATE TABLE users (
#     id SERIAL PRIMARY KEY,
#     email VARCHAR(255) UNIQUE NOT NULL,
#     age INT,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );

# 4. Удалить таблицу
# DROP TABLE users;

# 5. Добавить данные в таблицу
# INSERT INTO accounts_user (email, password, first_name)
# VALUES ('test@mail.com', '2003', 'Hoji');

user = User.objects.create_user(
    full_name = 'Marcus',
    age = 16,
    email = 'maaaarcusmoraes@gmail.com',
    role = 'admin',
    password = '12345678mm',
)

user.is_staff = True
user.save()


# 6. Добавить несколько записей
# INSERT INTO users (email, age)
# VALUES 
# ('a@mail.com', 20),
# ('b@mail.com', 30);

users = [
    User.objects.create_user(
        full_name = 'Ryan',
        age = 17,
        email = 'a@gmail.com',
        role = 'manager',
        password = '12345678rg'
),
    User.objects.create_user(
        full_name = 'Artem',
        age = 26,
        email = 'artemfrommetro@mail.ru',
        role = 'admin',
        password = '12345678afm'
    )
]

for user in users:
    user.is_staff = True
    user.save()


# 7. Выбрать все данные
# SELECT * FROM users;

users = User.objects.all()

# 8. Выбрать конкретные колонки
# SELECT email, age FROM users;

specific_user = User.objects.values('email', 'age')

# 9. Фильтрация с WHERE
# SELECT * FROM users WHERE age > 18;

age_filter = User.objects.filter(age__gt=18)

# 10. Несколько условий (AND)
# SELECT * FROM users WHERE age > 18 AND age < 30;

age_filtered_users = User.objects.filter(age__range=[18, 30])

# 11. Логическое ИЛИ (OR)
# SELECT * FROM users WHERE age = 20 OR age = 30;

from django.db.models import Q

twenty_or_thirty_users = User.objects.filter(Q(age=20) |Q(age=30) )

# 12. Сортировка данных
# SELECT * FROM users ORDER BY age DESC;

descending_age_filter = User.objects.order_by('-age')

# 13. Ограничение количества строк
# SELECT * FROM users LIMIT 5;

first_five_users = User.objects.all()[:5]

# 14. Пропуск строк (пагинация)
# SELECT * FROM users LIMIT 5 OFFSET 5;

missing_users = User.objects.all()[5:10]

# 15. Обновление данных
# UPDATE users SET age = 26 WHERE email = 'test@mail.com';

updated_users = User.objects.filter(email='maaaarcusmoraes@gmail.com').update(age=17)

# 16. Удаление записи
# DELETE FROM users WHERE email = 'test@mail.com';

deleted_users = User.objects.filter(email='a@gmail.com').delete()

# 17. Подсчёт количества строк
# SELECT COUNT(*) FROM users;

count_strs = User.objects.count()

# 18. Уникальные значения
# SELECT DISTINCT age FROM users;

distinct_ages = User.objects.filter('age').distinct()

# 19. Диапазон значений
# SELECT * FROM users WHERE age BETWEEN 20 AND 30;

age_ranged_users = User.objects.filter(age__range=[20, 31])

# 20. Поиск по шаблону
# SELECT * FROM users WHERE email LIKE '%mail.com';

similar_emails = User.objects.filter(email__endswith='@gmail.com')

# 21. Проверка на список значений
# SELECT * FROM users WHERE age IN (20, 25, 30);

specific_age_of_users = User.objects.filter(Q(age=20) | Q(age=25) | Q(age=30))

# 22. Проверка на NULL
# SELECT * FROM users WHERE age IS NULL;

null_age_info_users = User.objects.filter(age__isnull=True)

# 23. Создание таблицы с внешним ключом
# CREATE TABLE orders (
#     id SERIAL PRIMARY KEY,
#     user_id INT REFERENCES users(id),
#     total_price DECIMAL(10,2)
# );

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)


# 24. JOIN (объединение таблиц)
# SELECT users.email, orders.total_price
# FROM users
# JOIN orders ON users.id = orders.user_id;

orders = Order.objects.select_related('user').values(
    'user__email',
    'total_price'
)

# 25. GROUP BY + COUNT
# SELECT age, COUNT(*)
# FROM users
# GROUP BY age;

from django.db.models import Count

age_stats = User.objects.values('age').annotate(count=Count('id'))