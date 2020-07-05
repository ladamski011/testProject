from app import db
from app.models import User, Post

#
# u = User(username='john', email='john@example.com')
# db.session.add(u)
# db.session.commit()

# u = User(username='susan', email='susan@example.com')
# db.session.add(u)
# db.session.commit()

u = User.query.get(1)
# p = Post(body='my first post!', author=u)
# db.session.add(p)
# db.session.commit()
# print(u.posts.all())


users = User.query.all()
for u in users:
    db.session.delete(u)

posts = Post.query.all()
for p in posts:
    db.session.delete(p)

db.session.commit()