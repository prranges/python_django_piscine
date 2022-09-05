#!/usr/local/bin/python3

from elem import Elem, Text


class Html(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='html', attr=attr, content=content, tag_type='double')


class Head(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='head', attr=attr, content=content, tag_type='double')


class Body(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='body', attr=attr, content=content, tag_type='double')


class Title(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='title', attr=attr, content=content, tag_type='double')


class Meta(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='meta', attr=attr, content=content, tag_type='simple')


class Img(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='img', attr=attr, content=content, tag_type='simple')


class Table(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='table', attr=attr, content=content, tag_type='double')


class Th(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='th', attr=attr, content=content, tag_type='double')


class Tr(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='tr', attr=attr, content=content, tag_type='double')


class Td(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='td', attr=attr, content=content, tag_type='double')


class Ul(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='ul', attr=attr, content=content, tag_type='double')


class Ol(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='ol', attr=attr, content=content, tag_type='double')


class Li(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='li', attr=attr, content=content, tag_type='double')


class H1(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='h1', attr=attr, content=content, tag_type='double')


class H2(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='h2', attr=attr, content=content, tag_type='double')


class P(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='p', attr=attr, content=content, tag_type='double')


class Div(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(attr=attr, content=content, tag_type='double')


class Span(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='span', attr=attr, content=content, tag_type='double')


class Hr(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='hr', attr=attr, content=content, tag_type='double')


class Br(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='br', attr=attr, content=content, tag_type='double')


def test():
    print('---***---')
    print(
        Html([
            Head([
                Title(Text('“Hello ground!”')),
                Meta(attr={'charset': 'utf-8'})
            ]),
            Body([
                H2(Text('Header 2')),
                Hr(),
                P(Text('Lorem ipsum')),
                Table([
                    Tr([Th(Text('1')), Th(Text('2'))]),
                    Tr([Td(Text('3')), Td(Text('4'))])
                ]),
                Ul([
                    Li(Text('ol1')),
                    Li(Text('ol2'))
                ]),
                Ol([
                    Li(Text('ol1')),
                    Li(Text('ol2'))
                ]),
                Div(Text('text in div')),
                Br(),
                Br(),
                Span(Text('text in span')),
            ])
        ])
    )
    print('---***---')
    print(Html([Head(), Body()]))
    print('---***---')
    print(
        Html([
            Head(
                Title(Text('“Hello ground!”'))
            ),
            Body([
                H1(Text('“Oh no, not again!”')),
                Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})
            ])
        ])
    )
    print('---***---')


if __name__ == '__main__':
    test()