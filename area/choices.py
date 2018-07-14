class LevelDangerous(object):
    LOW = 1
    MIDDLE = 2
    HIGH = 3
    NOT = 4

    CHOICES = (
        (LOW, 'низкий'),
        (MIDDLE, 'средний'),
        (HIGH, 'высокий'),
        (NOT, 'нет')
    )

    DICT = dict(CHOICES)
