"""A model with methods that sets my profile information"""
from datetime import datetime, timezone
import requests


def get_facts():
    """Fetches Cat Facts from external API"""
    url = "https://catfact.ninja/fact"
    try:
        response = requests.get(url, timeout=(10, 10))

        # Raise an HTTPError for bad responses
        response.raise_for_status()

        response_dict = response.json()
        fact = response_dict['fact']
        return fact
    except requests.exceptions.Timeout:
        return "The request timed out"
    except requests.exceptions.ConnectionError:
        return "Failed to connect. Check your internet connection"
    except requests.exceptions.HTTPError as e:
        return f"HTTP error occurred: {e}"
    except requests.exceptions.RequestException as e:
        # Catch all other exceptions.
        return f"An unexpected error occurred: {e}"


class Profile:
    """The Profile class that contains my basic information"""
    def __init__(self):
        self.status = "success"
        self.email = "kwekuannan.dev@gmail.com"
        self.name = "Emmanuel Adu Saah"
        self.stack = ["Python", "Django", "Flask", "Go/Gin"]
        self.timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
        self.facts = get_facts()

    def profile_dict(self):
        profile = {
            "status": "success",
            "user": {
                "email": self.email,
                "name": self.name,
                "stack": self.stack
            },
            "timestamp": self.timestamp,
            "fact": self.facts
        }
        return profile
