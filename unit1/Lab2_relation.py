class User:
    def __init__(self, name, surname, username, password):
        self.name = name
        self.surname = surname
        self.username = username
        self._password = password
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print(f"The user {self.username} created a post.")

    def show_posts(self):
        print(f"\nPosts by {self.username}:")
        for post in self.posts:
            post.print_post()


class Post:
    def __init__(self, description, user, likes=0):
        self.description = description
        self.likes = likes
        self.user = user

    def increment_likes(self):
        self.likes += 1

    def print_post(self):
        print(f"[{self.likes} likes] {self.user.username}: {self.description}")


class Comments:
    def __init__(self, comment, user, post, likes=0):
        self.comment = comment
        self.likes = likes
        self.user = user
        self.post = post

    def show_comment(self):
        print(f"{self.user.username} commented: '{self.comment}' ({self.likes} likes)")


class Message:
    def __init__(self, text, sender, receiver):
        self.text = text
        self.sender = sender
        self.receiver = receiver

    def send(self):
        print(f"Message from {self.sender.username} to {self.receiver.username}: {self.text}")


# Instances
user_galileo = User("Gael", "Torres", "galileo", "pass")
user_carlos = User("Carlos", "Silva", "carlos_p", "abcd")

post_galileo = Post("ex test", user_galileo, likes=3)
user_galileo.add_post(post_galileo)

comment = Comments("comment", user_carlos, post_galileo, likes=1)
comment.show_comment()

message = Message("msg", user_carlos, user_galileo)
message.send()

user_galileo.show_posts()
