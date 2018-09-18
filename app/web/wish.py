from flask import current_app,flash,redirect,url_for,render_template
from flask_login import login_required,current_user
from app.models.base import db
from app.view_models.trade import MyTrades
from app.view_models.wish import MyWishes

from . import web

__author__ = '七月'


@web.route('/my/wish')
def my_wish():
    from app.models.wish import Wish
    uid = current_user.id
    wishes_of_mine = Wish.get_user_wishes(uid)
    isbn_list=[wish.isbn for wish in wishes_of_mine]
    gift_count_list = Wish.get_gift_counts(isbn_list)
    # view_model = MyWishes(wishes_of_mine, gift_count_list)
    view_model = MyTrades(wishes_of_mine, gift_count_list)

    return render_template('my_wish.html', wishes=view_model.trades)



@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    from app.models.wish import Wish
    if current_user.can_save_to_list(isbn):
        try:
            wish = Wish()
            wish.isbn=isbn
            wish.uid = current_user.id
            db.session.add(wish)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
    else:
        flash('这本书已添加至你的赠送清单或已存在你的心愿清单，请不要重复添加')
    return redirect(url_for('web.book_detail',isbn=isbn))


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
