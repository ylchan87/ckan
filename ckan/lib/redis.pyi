from redis import Redis

REDIS_URL_SETTING_NAME: str
REDIS_URL_DEFAULT_VALUE: str

def connect_to_redis() -> Redis: ...
def is_redis_available() -> bool: ...
