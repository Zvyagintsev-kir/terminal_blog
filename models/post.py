class Post(object):

    def __init__(self, blog_id, title, content, author, date, id):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.create_date = date
        self.id = id

    def save_to_mongo(self):
        pass

    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.create_date
        }
