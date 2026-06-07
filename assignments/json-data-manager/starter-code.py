import json
from pathlib import Path
from typing import Dict, List, Optional

DATA_FILE = Path(__file__).parent / "users.json"

User = Dict[str, object]


def load_users() -> List[User]:
    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_users(users: List[User]) -> None:
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(users, file, indent=2)


def add_user(name: str, email: str) -> User:
    users = load_users()
    next_id = max((user["id"] for user in users), default=0) + 1
    new_user = {"id": next_id, "name": name, "email": email}
    users.append(new_user)
    save_users(users)
    return new_user


def update_user_email(user_id: int, new_email: str) -> Optional[User]:
    users = load_users()
    for user in users:
        if user["id"] == user_id:
            user["email"] = new_email
            save_users(users)
            return user
    return None


def filter_users_by_domain(domain: str) -> List[User]:
    users = load_users()
    return [user for user in users if user["email"].endswith(domain)]


if __name__ == "__main__":
    print(load_users())
    print(add_user("Dana", "dana@example.com"))
    print(update_user_email(1, "alice@newdomain.com"))
    print(filter_users_by_domain("example.com"))
