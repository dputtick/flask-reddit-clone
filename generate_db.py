import json
from app import db, User, Post

users = {1: {
                    'username': 'firstuser',
                    'password': '1234',
                    'email': 'fu@gmail.com'},
        4: {
                    'username': 'test',
                    'password': '5678',
                    'email': 'test@gmail.com'}
        }




posts = {
        2: {
                    'title': 'Post #1',
                    'poster': 1,
                    'content': 'Post content for post 1',
                    'upvotes': 10,
                    'downvotes': 8},
        3: {
                    'title': 'Post #2',
                    'poster': 1,
                    'content': 'More content here'},
        5: {
                    'title': 'Post #3',
                    'poster': 1,
                    'content': 'Some super content'},
        6: {
                    'title': 'Post #4',
                    'poster': 1,
                    'content': 'Incredible content'},
        7: {
                    'title': 'Post #5',
                    'poster': 1,
                    'content': 'Look, content!'},
        8: {
                    'title': 'Post #6',
                    'poster': 1,
                    'content': 'This one isn\'t very compelling'},
        9: {
                    'title': 'Post #7',
                    'poster': 1,
                    'content': 'Woo last test content'},
        10: {
                    'title': 'Post #1',
                    'poster': 1,
                    'content': 'Post content for post 1'},
        11: {
                    'title': 'Post #2',
                    'poster': 1,
                    'content': 'More content here'},
        12: {
                    'title': 'Post #3',
                    'poster': 1,
                    'content': 'Some super content'},
        13: {
                    'title': 'Post #4',
                    'poster': 1,
                    'content': 'Incredible content'},
        14: {
                    'title': 'Post #5',
                    'poster': 1,
                    'content': 'Look, content!'},
        15: {
                    'title': 'Post #6',
                    'poster': 1,
                    'content': 'This one isn\'t very compelling'},
        16: {
                    'title': 'Post #7',
                    'poster': 1,
                    'content': 'Woo last test content'},
        17: {
                    'title': 'Post #1',
                    'poster': 1,
                    'content': 'Post content for post 1'},
        18: {
                    'title': 'Post #2',
                    'poster': 1,
                    'content': 'More content here'},
        19: {
                    'title': 'Post #3',
                    'poster': 1,
                    'content': 'Some super content'},
        20: {
                    'title': 'Post #4',
                    'poster': 1,
                    'content': 'Incredible content'},
        21: {
                    'title': 'Post #5',
                    'poster': 1,
                    'content': 'Look, content!'},
        22: {
                    'title': 'Post #6',
                    'poster': 1,
                    'content': 'This one isn\'t very compelling'},
        23: {
                    'title': 'Post #7',
                    'poster': 1,
                    'content': 'Woo last test content'},
        24: {
                    'title': 'Post #1',
                    'poster': 1,
                    'content': 'Post content for post 1'},
        25: {
                    'title': 'Post #2',
                    'poster': 1,
                    'content': 'More content here'},
        26: {
                    'title': 'Post #3',
                    'poster': 1,
                    'content': 'Some super content'},
        27: {
                    'title': 'Post #4',
                    'poster': 1,
                    'content': 'Incredible content'},
        28: {
                    'title': 'Post #5',
                    'poster': 1,
                    'content': 'Look, content!'},
        29: {
                    'title': 'Post #6',
                    'poster': 1,
                    'content': 'This one isn\'t very compelling'},
        30: {
                    'title': 'Post #7',
                    'poster': 1,
                    'content': 'Woo last test content'}
        }


def main():
    db.create_all()
    for id, user_data in users.items():
        user = User(id=id, username=user_data['username'])
        db.session.add(user)
    for id, post_data in posts.items():
        post = Post(id=id, 
                    poster_id=post_data['poster'], 
                    content=post_data['content'],
                    title=post_data['title'])
        db.session.add(post)
    db.session.commit()


if __name__ == '__main__':
    main()

# with open('users.json', 'r') as f:
#     users = json.load(f)

# print(users)

# with open('db.json', 'w') as f:
#     json.dump(posts, f)

# with open('users.json', 'w') as f:
#     json.dump(users, f)
