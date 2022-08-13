from sqlalchemy import Column,Integer,String,ForeignKey
from blog.database import Base
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer,primary_key = True,index=True)
    title = Column(String(255))
    body = Column(String(255))
    user_id = Column(Integer,ForeignKey('users.id'))
    author = relationship("User",back_populates="blogs")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key = True,index=True)
    name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    blogs = relationship("Blog",back_populates="author")

    