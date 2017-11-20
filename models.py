import peewee
database= peewee.SqliteDatabase('user_info.db')

def initialize_db():
    database.create_tables([User,Media,Comment],safe=True)

class User(peewee.Model):
    user_id= peewee.CharField()
    username= peewee.CharField()
    follows_count = peewee.IntegerField()
    full_name= peewee.CharField()
    followed_by_count=peewee.IntegerField()
    class Meta:
        database=database
    new_user= User(user_id=5,username='acadview',full_name='Acadview',follows_count=20)
    new_user.save()
class Media:
        user_id=peewee.ForeignKeyField(User,to_field="user_id")
        media_id=peewee.CharField(unique=True)
        media_type=peewee.CharField()
        media_link = peewee.CharField()
    class Meta:
        database=database

class Comment(peewee.Model):
    comment_id = peewee.CharField(unique=True)
    media_id = peewee.ForeignKeyField(Media, to_field="media_id")
    user_id = peewee.ForeignKeyField(User, to_field="user_id")
    comment_text = peewee.CharField()

    class Meta:
        database = database