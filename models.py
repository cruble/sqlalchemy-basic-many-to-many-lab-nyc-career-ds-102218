from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

# Write your classes below


class Actor(Base):
	__tablename__ = 'actors'

	id = Column(Integer, primary_key=True)
	name = Column(Text)

	roles = relationship('Role', secondary='actor_roles')

class Role(Base):
	__tablename__ = 'roles'
	
	id = Column(Integer, primary_key=True)
	character = Column(Text)

	actors = relationship('Actor', secondary='actor_roles')

class ActorRole(Base):
	__tablename__ = 'actor_roles'

	id = Column(Integer, primary_key=True)
	role_id = Column(Integer, ForeignKey('roles.id'))
	actor_id = Column(Integer, ForeignKey('actors.id'))



engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
session = sessionmaker()
session.configure(bind=engine)

session = session()

