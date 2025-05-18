import joblib
from datetime import datetime, timedelta
from collections import defaultdict
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(name="X-API-Key")
# allow multiple API keys for different users 
API_KEYS = {
    "abc123": "User A",
    "def456": "User B",
    "ghi789": "User C"
}

# Model creation
model = joblib.load("sentiment_model.joblib")


class RateLimiter:
    def __init__(self, requests_per_minute: int = 10):
        self.requests_per_minute = requests_per_minute
        self.requests = defaultdict(list)  # Store request timestamps per API key

    def is_rate_limited(self, api_key: str) -> tuple[bool, int]:
        """
        Check if the request should be rate limited
        Returns (is_limited, requests_remaining)
        """
        now = datetime.now()
        minute_ago = now - timedelta(minutes=1)
        
        # Remove requests older than 1 minute
        self.requests[api_key] = [
            req_time for req_time in self.requests[api_key]
            if req_time > minute_ago
        ]
        
        # Check if rate limit is exceeded
        recent_requests = len(self.requests[api_key])
        if recent_requests >= self.requests_per_minute:
            return True, 0
            
        # Add new request timestamp
        self.requests[api_key].append(now)
        return False, self.requests_per_minute - recent_requests - 1
