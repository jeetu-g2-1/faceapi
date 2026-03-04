from django.core.management.base import BaseCommand
from api1.models import APIKey
import uuid
import hashlib

class Command(BaseCommand):
    help="Create a new API key"
    
    def handle(self, *args, **kwargs):

        #Ask user for API key name
        name=input("Enter API Key name: ").strip()

        if not name:
            self.stdout.write(self.style.ERROR("API key name cannot be empty"))
            return
        
        #Generate API key
        raw_key= uuid.uuid4().hex

        # Hash the key
        hashed_key=hashlib.sha256(raw_key.encode()).hexdigest()

        #Store in DB
        APIKey.objects.create(
            name=name,
            hashed_key=hashed_key
        )

        #output
        self.stdout.write(self.style.SUCCESS("API Key created successfully!"))
        self.stdout.write(self.style.WARNING(f"API Key: {raw_key}"))
        self.stdout.write("Save this key securely. It will not be shown again.")