from src.models.test import Test


class TestService:
    """Service for testing."""

    def ping(self):
        return Test(name='pong')


async def get_test_service():
    """Get a service for working with Genre data"""
    return TestService()
