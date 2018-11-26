import babel

def format_datetime(value, format='yyyy-MM-dd HH:mm:ss'):
    return babel.dates.format_datetime(value, format)

