from models.post import Post
from database import Database

Database.initialize()

post = Post(blog_id="123",
            title="Another greate post",
            content="This is some sample content",
            author="kzv")

# another comment
post.save_to_mongo()




