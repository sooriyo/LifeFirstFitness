from database import Base, engine
from models.admin import Admin


def create_database():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_database()
    print("Database tables created.")
