"""
User model for the Flask application.
Equivalent to the Java User class in Spring Boot.
"""


class User:
    """User model with id, name, email, age, and city attributes."""
    
    def __init__(self, id=None, name=None, email=None, age=None, city=None):
        """
        Initialize a User instance.
        
        Args:
            id (int): User ID
            name (str): User's full name
            email (str): User's email address
            age (int): User's age
            city (str): User's city
        """
        self.id = id
        self.name = name
        self.email = email
        self.age = age
        self.city = city
    
    def to_dict(self):
        """
        Convert User instance to dictionary for JSON serialization.
        
        Returns:
            dict: User data as dictionary
        """
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'age': self.age,
            'city': self.city
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Create User instance from dictionary.
        
        Args:
            data (dict): User data dictionary
            
        Returns:
            User: New User instance
        """
        return cls(
            id=data.get('id'),
            name=data.get('name'),
            email=data.get('email'),
            age=data.get('age'),
            city=data.get('city')
        )
    
    def __repr__(self):
        """String representation of User instance."""
        return f"User(id={self.id}, name='{self.name}', email='{self.email}', age={self.age}, city='{self.city}')"


# Made with Bob