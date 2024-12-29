from .app import db
from sqlalchemy.dialects.postgresql import JSON


class TeamMember(db.Model):
    __tablename__ = 'team_members'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(128), nullable=False)
    bio = db.Column(db.Text, nullable=True)  # Added 'bio' field
    image_url = db.Column(db.String(256), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role,
            "bio": self.bio,
            "image_url": self.image_url
        }


class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(256), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "image_url": self.image_url,
            "created_at": self.created_at
        }


class Home(db.Model):
    __tablename__ = 'home'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    subtitle = db.Column(db.String(256), nullable=False)
    image_url = db.Column(db.String(256), nullable=True)
    content = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "subtitle": self.subtitle,
            "image_url": self.image_url,
            "content": self.content
        }


class About(db.Model):
    __tablename__ = 'about'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)  # Added 'title' field
    content = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content
        }


class Service(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)  # Changed 'title' to 'name'
    description = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }


class Contact(db.Model):
    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(256), nullable=True)  # Added 'address' field
    phone = db.Column(db.String(64), nullable=True)  # Added 'phone' field
    email = db.Column(db.String(128), nullable=False)
    social_links = db.Column(JSON, nullable=True)  # Added 'social_links' field

    def to_dict(self):
        return {
            "id": self.id,
            "address": self.address,
            "phone": self.phone,
            "email": self.email,
            "social_links": self.social_links
        }


class FAQ(db.Model):
    __tablename__ = 'faqs'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(256), nullable=False)
    answer = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "question": self.question,
            "answer": self.answer
        }
