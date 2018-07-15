class ComplintStatus(object):
    PROCESSING = 1
    CLOSED = 2

    CHOICES = (
        (PROCESSING, 'обрабатывается'),
        (CLOSED, 'закрыт'),
    )

    DICT = dict(CHOICES)
