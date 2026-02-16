"""
User model for the Flask application.
Equivalent to the Java User class from the Spring Boot application.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    """
    User data class representing a user entity.
    
    Attributes:
        id: Unique identifier for the user
        name: Full name of the user
        email: Email address of the user
        age: Age of the user
        city: City where the user resides
    """
    id: int
    name: str
    email: str
    age: int
    city: str

    def to_dict(self):
        """Convert User object to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'age': self.age,
            'city': self.city
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Create User object from dictionary."""
        return cls(
            id=int(data['id']),
            name=str(data['name']),
            email=str(data['email']),
            age=int(data['age']),
            city=str(data['city'])
        )

    def __repr__(self):
        """String representation of User object."""
        return f"User(id={self.id}, name='{self.name}', email='{self.email}', age={self.age}, city='{self.city}')"


# Made with Bob