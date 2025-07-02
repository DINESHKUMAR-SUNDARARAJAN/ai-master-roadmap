# memory_store.py
from collections import defaultdict

# In-memory dict to store per-user memory
USER_MEMORY = defaultdict(list)

def get_memory(user_id: str) -> list:
    return USER_MEMORY[user_id]

def add_to_memory(user_id: str, message) -> None:
    USER_MEMORY[user_id].append(message)