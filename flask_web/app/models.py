#!/usr/bin/python
# -*- coding: utf-8 -*-
from . import db, login_manage
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_moment import datetime
from markdown import markdown
import bleach



@login_manage.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#权限
class Permission():
    FOLLOW = 0x01
    COMMENT = 0X02
    WRITE_ARTICLES = 0x04
    MODERATE_COMMENTS = 0x08
    ADMINISTER = 0x80

class Follow(db.Model):
    __tablename__ = 'follows'
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    followed_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

#角色
class Role(db.Model):
    '''定义角色的数据库模型'''
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)      #是否为默认角色（普通用户）
    permissions = db.Column(db.Integer)        #设置权限
    user = db.relationship('User', backref='role', lazy='dynamic') #自身添加一个user属性，反过来给User添加一个role属性。属性可以赋值。

    @staticmethod
    def insert_roles():
        '''创建用户，版主和管理员三个角色的静态方法。'''
        roles = {
            "User": (Permission.FOLLOW | Permission.COMMENT | Permission.WRITE_ARTICLES, True),
            "Moderator": (Permission.FOLLOW | Permission.COMMENT | Permission.WRITE_ARTICLES |
                          Permission.MODERATE_COMMENTS, False),
            "Administrator": (0xff, False)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        '''打印角色名字'''
        return '<Role %r>' % self.name


#用户
class User(UserMixin, db.Model):
    '''定义使用者的数据库模型'''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    #为user表中添加添加一行外键，由该属性可以获得使用者的角色所对应的id值。

    confirmed = db.Column(db.Boolean, default=False)
    #增加一个确认属性
    password_hash = db.Column(db.String(128))

    #用户资料
    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    about_me = db.Column(db.Text())
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)
    #为文章列表添加反向键
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    # comments = db.relationship('Comment', backref='author', lazy='dynamic')

    #实现多对多关系表
    followed = db.relationship('Follow', foreign_keys=[Follow.follower_id],
                               backref=db.backref('follower', lazy='joined'),
                               lazy='dynamic',
                               cascade='all, delete-orphan')

    followers = db.relationship('Follow', foreign_keys=[Follow.followed_id],
                               backref=db.backref('followed', lazy='joined'),
                                lazy='dynamic',
                               cascade='all, delete-orphan')

    def __init__(self, **kwargs):
        '''每个用户对象被调用时都会调用该方法。如果该用户没有被赋予角色，则判断是否为管理员，给与管理员或者默认角色'''
        super(User, self).__init__(**kwargs)
        if self.role is None:
            if self.email == current_app.config['FLASK_ADMIN']:
                self.role = Role.query.filter_by(permissions=0xff).first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()


    def follow(self, user):
        if not self.is_following(user):
            f = Follow(follower=self, followed=user)
            db.session.add(f)

    def unfollow(self, user):
        f = self.followed.filter_by(followed_id=user.id).first()
        if f:
            db.session.delete(f)

    def is_following(self, user):
        return self.followed.filter_by(followed_id=user.id).first() is not None

    def is_followed_by(self, user):
        return self.followers.filter_by(follower_id=user.id).first() is not None

    def ping(self):
        '''载入最后一次访问的日期'''
        self.last_seen = datetime.utcnow()
        db.session.add(self)

    def can(self, permissions):
        '''验证用户是否拥有该权限的方法'''
        return self.role is not None and ((self.role.permissions & permissions) == permissions)

    def is_administrator(self):
        '''验证是否为管理员的方法'''
        return self.can(Permission.ADMINISTER)


    #对密码进行哈希处理，密码无法直接读取
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=3600):
        #此函数生成令牌，返回token
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        #此函数用来确认令牌，据此返回True或者False，并改变confirmed的值
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    @staticmethod
    def generate_fake(count=100):
        from sqlalchemy.exc import IntegrityError
        from random import seed
        import forgery_py

        seed()
        for i in range(count):
            u = User(
                email=forgery_py.internet.email_address(),
                username=forgery_py.internet.user_name(),
                password='li',
                confirmed=True,
                name=forgery_py.name.full_name(),
                location=forgery_py.address.city(),
                about_me=forgery_py.lorem_ipsum.sentence(),
            )
            db.session.add(u)
            try:
                db.session.commit()
            except:
                db.session.rollback()

    #使用表的联结返回所关注对象的文章列表。
    @property
    def followed_posts(self):
        return Post.query.join(Follow, Follow.followed_id == Post.author_id).filter(Follow.follower_id == self.id)

    @staticmethod
    def add_self_follow():
        for user in User.query.all():
            if not user.is_following(user):
                user.follow(user)
                db.session.add(user)
                db.session.commit()

    def __repr__(self):
        '''打印使用者的名字'''
        return '<User %r>' % self.username


#未登录用户
class AnonymousUser(AnonymousUserMixin):
    '''创建匿名用户类，实现can与is_administrator方法，实习多态，将未登陆的用户归为此类'''
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False


#文章模型
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))               #关联到User模型
    # comments = db.relationship('Comment', backref='post', lazy='dynamic')

    @staticmethod
    def generate_fake(count=100):
        from random import seed, randint
        import forgery_py

        seed()
        user_count = User.query.count()
        for i in range(count):
            u = User.query.offset(randint(0, user_count-1)).first()
            p = Post(body=forgery_py.lorem_ipsum.sentences(randint(1, 3)),
                     author=u)
            db.session.add(p)
            db.session.commit()

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                        'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
                        'h1', 'h2', 'h3', 'p']
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'),
                                                       tags=allowed_tags, strip=True))



db.event.listen(Post.body, 'set', Post.on_changed_body)


login_manage.anonymous_user = AnonymousUser             #将未登陆的用户归为AnonymousUser类



#因为数据库原因，暂时取消文章评论功能
# class Comment(db.Model):
#     __tablename__ = 'comments'
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.Text)
#     body.html = db.Column(db.Text)
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     disabled = db.Column(db.Boolean)
#     author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
#
#     @staticmethod
#     def on_changed_body(target, value, oldvalue, initiator):
#         allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
#                         'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
#                         'h1', 'h2', 'h3', 'p']
#         target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'),
#                                                        tags=allowed_tags, strip=True))
#
# db.event.listen(Comment.body, 'set', Comment.on_changed_body)






















