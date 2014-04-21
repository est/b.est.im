import datetime
import peewee


class User(peewee.Model):
    name = peewee.CharField()
    date_joined = peewee.DateTimeField(default=datetime.datetime.utcnow())
    status = peewee.IntegerField(choices=[
        (0, 'normal'),
        (1, 'deactivated'),
        (2, 'waiting email confirm'),
        (3, 'token expired'),
    ], default=2)


class Post(peewee.Model):
    title = peewee.CharField()
    content = peewee.TextField()
    content_type = peewee.IntegerField(max_length=1, choices=[
        ('d', 'markdown'),
        ('h', 'html'),
        ('t', 'text'),
    ], default='d')
    author = peewee.ForeignKeyField(User, ondelete='SET_NULL')
    date_created = peewee.DateTimeField(default=datetime.datetime.utcnow())


class PostComment(peewee.Model):
    content = peewee.TextField()
    content_type = peewee.IntegerField(max_length=1, choices=[
        ('d', 'markdown'),
        ('h', 'html'),
        ('t', 'text'),
    ], default='d')
    author = peewee.ForeignKeyField(User, ondelete='SET_NULL')
    date_created = peewee.DateTimeField(default=datetime.datetime.utcnow())
