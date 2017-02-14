import inspect
import logging
import logging.config

def get_module_name(depth=1):
    frame = inspect.currentframe()
    one_up = inspect.getouterframes(frame)[depth]
    filename = one_up[1]
    modulename = inspect.getmodulename(filename)

    del frame, one_up

    return modulename


def get_logger(name=None):
    if name is None:
        name = get_module_name(2)

    logging.config.dictConfig({
        'version': 1,
        'formatters': {
            'verbose': {
                'format': ('[%(levelname)8s %(asctime)s] %(message)s'),
            },
        },
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'formatter': 'verbose',
                'class': 'logging.FileHandler',
                'filename': '%s.debug.log' % name,
            },
            'console': {
                'level': 'INFO',
                'formatter': 'verbose',
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            name: {
                'level': 'DEBUG',
                'handlers': ['file', 'console'],
            },
        },
    })

    return logging.getLogger(name)

