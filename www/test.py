import orm
from models import User, Blog, Comment
import asyncio

def test():
    loop = asyncio.get_event_loop()
    orm.create_pool(loop=loop, host='127.0.0.1', port=3306, user='root', password='techain,SW14', db='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    u.save()