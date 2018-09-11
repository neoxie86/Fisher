# -*- coding:utf-8 -*-
__author__ = 'neo'
__time__ = '2018/9/8 11:43'

class BookViewModel:
    def __init__(self,book):
        self.title = book['title']
        self.publisher =book['publisher']
        self.pages = book['pages']
        self.author = book['author']
        self.price = book['price']
        self.summary = book['summary']
        self.image = book['image']

class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self,yushu_book,keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]


class __BookViewModel:
    @classmethod
    def packge_single(cls,data,keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword':keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]
        return returned

    @classmethod
    def packge_collection(cls,data,keyword):
        returned = {
            'books':[],
            'total':0,
            'keyword':keyword
        }
        if data:
            returned['total'] = data['total'],
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return returned

    @classmethod
    def __cut_book_data(cls,data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'author': '、'.join(data['author']),
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image']
        }
        return book

    @classmethod
    def __cut_books_data(cls, data):
        books = []
        for book in data['books']:
            r = {
                'title': data['tilte'],
                'publisher': data['publisher'],
                'pages': data['pages'],
                'author': '、'.join(data['author']),
                'price': data['price'],
                'summary': data['summary'],
                'image': data['image']

            }
            books.append(r)

        return books