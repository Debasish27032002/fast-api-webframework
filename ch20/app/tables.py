from db import engine
from sqlalchemy import MetaData, Table, Column, String, Integer, ForeignKey

metadata = MetaData()

# User Tabel
users = Table(
    "users",
    metadata, 
    Column("id",Integer, primary_key=True), # Auto increment for integer type primary key 
    Column("name", String(50), nullable=False ),
    Column("email",String, unique=True, nullable=False)
)


# Create relations - one to many 
posts = Table(
    "posts",
    metadata, 
    Column('id', Integer, primary_key=True),
    Column('user_id' , Integer, ForeignKey("users.id" ,ondelete = "CASCADE"), nullable=False),
    Column('title', String, nullable=False),
    Column('content',String , nullable=False)
)

# Create relation many to one
profile = Table(
    "profile",
    metadata, 
    Column('id', Integer, primary_key=True),
    Column('user_id' , Integer, ForeignKey("users.id" ,ondelete = "CASCADE"), nullable=False, unique=True), # make this unique true for making it one to one
    Column('bio', String, nullable=False),
    Column('address',String , nullable=False)
)

# Create relation  - many to many 
address = Table(
    "address",
    metadata, 
    Column("id",Integer, primary_key=True),
    Column("street", String, nullable=False),
    Column("country", String, nullable=False)
)
user_address_association = Table(
    "user_address_association",
    metadata, 
    Column('user_id', Integer, ForeignKey('users.id', ondelete="CASCADE"), primary_key=True),
    Column('address_id', Integer, ForeignKey('address.id', ondelete="CASCADE"), primary_key=True)
)

# Create table in database
def create_tables():
    metadata.create_all(engine)
    
# Drop all tables 
def drop_tables():
    metadata.drop_all(engine)