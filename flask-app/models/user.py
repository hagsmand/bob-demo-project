class User:
    """User model class"""
    
    def __init__(self, id=None, name=None, email=None, age=None, city=None):
        """Initialize User with all fields"""
        self.id = id
        self.name = name
        self.email = email
        self.age = age
        self.city = city
    
    def to_dict(self):
        """Convert User object to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'age': self.age,
            'city': self.city
        }
    
    @staticmethod
    def from_dict(data):
        """Create User object from dictionary"""
        return User(
            id=data.get('id'),
            name=data.get('name'),
            email=data.get('email'),
            age=data.get('age'),
            city=data.get('city')
        )
    
    def __repr__(self):
        """String representation of User"""
        return f"User(id={self.id}, name='{self.name}', email='{self.email}', age={self.age}, city='{self.city}')"

# Made with Bob