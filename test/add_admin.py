from sqlalchemy.orm import Session
from models.admin import Admin
from database import SessionLocal
import hashlib
import bcrypt


def hash_password(password: str):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def add_admin(username: str, password: str, email: str, role: str):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    db = SessionLocal()
    new_admin = Admin(username=username, hashed_password=hashed_password, email=email, role=role)

    try:
        db.add(new_admin)
        db.commit()
        print(f"Admin {username} added successfully.")
    except Exception as e:
        print(f"Failed to add admin {username}: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    # Example usage
    add_admin("sadeesha1", "sadees1ha", "sa1deesha@example.com", "admin_role")
