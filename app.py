from models.post import Post
from database import Database

Database.initialize()

# some new comment
post = Post(blog_id="123",
            title="Another greate post",
            content="This is some sample content",
            author="kzv")
post.save_to_mongo()

blog = Blog()

blog.new_post()
blog.save_to_mongo()

Blog.from_mongo()

blog.get_posts()




