"""A model with methods that sets my profile information"""
from datetime import datetime, timezone


class Profile:
    """The Profile class that contains my basic information"""
    def __init__(self):
        self.status = "success"
        self.email = "kwekuannan.dev@gmail.com"
        self.name = "Emmanuel Adu Saah"
        self.stack = ["Python", "Django", "Flask", "Go/Gin"]
        self.timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')