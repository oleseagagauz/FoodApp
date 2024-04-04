LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',  # Измените уровень на INFO
            'class': 'logging.StreamHandler',
            'formatter': 'colored'
        },
    },
    'formatters': {
        'colored': {
            '()': 'colorlog.ColoredFormatter',  # Используем цветной форматтер
            'format': '%(log_color)s[%(levelname)s] %(asctime)s %(message)s',
            'log_colors': {
                'DEBUG': 'cyan',
                'INFO': 'green',  # Зеленый цвет для INFO
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red,bg_white',
            }
        }
    },
    'loggers': {
        'django.server': {
            'handlers': ['console'],
            'level': 'INFO',  # Изменяем уровень на INFO
            'propagate': False,
        },
    },
}