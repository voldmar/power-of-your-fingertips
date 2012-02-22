# coding: utf-8

import re

import markdown
from jinja2 import Template

class FormatError(ValueError):
    pass


template = Template('''<!DOCTYPE HTML>
<html lang="en-US">
<head>
    <title>{{ title }}</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=1274, user-scalable=no">
    <link rel="stylesheet" href="shower/themes/ribbon/styles/style.css">
    <style>
        #Cover H2 {
            color:#FFF;
            text-align:center;
            font-size:70px;
            }
    </style>
</head>
<body class="list">
    <header class="caption">
        <h1>{{ title }}</h1>
        <p>Vladimir Epifanov, Ostrovok.ru</p>
    </header>
    {% for slide in slides %}
    <div class="slide" id="{{ slide.id }}"><div>
        <section>
            <header>
                <h2>{{ slide.header }}</h2>
            </header>
            {{ slide.body }}
        </section>
    </div></div>
    {% endfor %}
    <div class="progress"><div></div></div>
    <script src="shower/scripts/script.js"></script>
</body>
</html>
''')


def convert(source):
    if not isinstance(source, unicode):
        source = source.decode('utf-8')
    result = re.split(r'^=+\s*$', source, flags=re.MULTILINE)
    if len(result) < 2:
        raise FormatError('No header')
    elif len(result) > 2:
        raise FormatError('More then one header')

    title, body = result
    title = title.strip()
    body = body.strip()

    _slides = re.split(r'^\s*$\n(?=^\w.+$\n^-+\s*$)', body, flags=re.MULTILINE|re.UNICODE)
    slides = []
    for slide in _slides:
        header, body = map(unicode.strip, re.split(r'^-+\s*$', slide, maxsplit=1, flags=re.MULTILINE))
        try:
            id, header = header.split(': ') # Space is significant
        except ValueError:
            id = filter(unicode.isalnum, header)

        slides.append(dict(
            id=id,
            header=header,
            body=markdown.markdown(body, output_format='html5'),
        ))

    return template.render(title=title, slides=slides)

if __name__ == '__main__':
    from sys import argv
    with open(argv[1]) as source:
        with open(argv[2], 'wb') as destination:
            destination.write(convert(source.read()).encode('utf-8'))


