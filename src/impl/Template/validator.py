def validate_html(cls, value):
    if '<body>' not in value:
        raise ValueError('HTML must have a <body> tag')
    return value
