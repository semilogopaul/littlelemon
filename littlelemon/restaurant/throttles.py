from rest_framework.throttling import UserRateThrottle

class TenCallsPerMinute(UserRateThrottle):
    rate = '10/minute'