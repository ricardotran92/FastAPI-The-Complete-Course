import os
import sys
import argparse
from typing import List

# Ensure imports work when running from repository root
sys.path.append(os.path.dirname(__file__))

from database import engine, SessionLocal
import models


SAMPLE_TODOS = [
    {"title": "Go to store", "description": "To pick up eggs", "priority": 4, "complete": False},
    {"title": "Haircut", "description": "Need to get length 1mm", "priority": 3, "complete": False},
    {"title": "Feed dog", "description": "Make sure to use new food brand", "priority": 5, "complete": False},
    {"title": "Water plant", "description": "Inside and Outside plants", "priority": 4, "complete": False},
    {"title": "Learn something new", "description": "Learn to program", "priority": 5, "complete": False},
]


def setup_db() -> None:
    """Create database tables based on `models`."""
    models.Base.metadata.create_all(bind=engine)
    print("Database tables created (if not existing): todos")


def seed_db(force: bool = False) -> None:
    """Insert sample todos. If table already has rows, skip unless `force` is True."""
    session = SessionLocal()
    try:
        existing = session.query(models.Todos).count()
        if existing and not force:
            print(f"Skipping seed: table already has {existing} rows. Use --force to insert anyway.")
            return

        for item in SAMPLE_TODOS:
            todo = models.Todos(
                title=item["title"],
                description=item["description"],
                priority=item["priority"],
                complete=item["complete"],
            )
            session.add(todo)
        session.commit()
        print(f"Seeded {len(SAMPLE_TODOS)} todos")
    finally:
        session.close()


def add_todo(title: str, description: str, priority: int = 1, complete: bool = False) -> None:
    session = SessionLocal()
    try:
        todo = models.Todos(title=title, description=description, priority=priority, complete=complete)
        session.add(todo)
        session.commit()
        print(f"Added todo id={todo.id} title={title}")
    finally:
        session.close()


def list_todos() -> List[models.Todos]:
    session = SessionLocal()
    try:
        rows = session.query(models.Todos).order_by(models.Todos.id).all()
        if not rows:
            print("No todos found. Use 'seed' or 'add' to create entries.")
            return []

        print(f"{'Id':<3} {'Title':<22} {'Description':<32} {'Priority':<8} {'Complete':<8}")
        print("-" * 90)
        for r in rows:
            print(f"{r.id:<3} {r.title:<22} {r.description:<32} {r.priority!s:<8} {int(r.complete):<8}")
        return rows
    finally:
        session.close()


def main():
    parser = argparse.ArgumentParser(description="CLI for managing the TodoApp SQLite database using SQLAlchemy")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("setup", help="Create tables")
    seed_p = sub.add_parser("seed", help="Insert sample todos")
    seed_p.add_argument("--force", action="store_true", help="Force insert even if table not empty")

    add_p = sub.add_parser("add", help="Add a single todo")
    add_p.add_argument("--title", required=True, help="Title of the todo")
    add_p.add_argument("--description", default="", help="Description")
    add_p.add_argument("--priority", type=int, default=1, help="Priority as integer")
    add_p.add_argument("--complete", action="store_true", help="Mark as complete")

    sub.add_parser("list", help="List all todos")

    args = parser.parse_args()

    if args.cmd == "setup":
        setup_db()
    elif args.cmd == "seed":
        seed_db(force=getattr(args, "force", False))
    elif args.cmd == "add":
        add_todo(args.title, args.description, args.priority, getattr(args, "complete", False))
    elif args.cmd == "list":
        list_todos()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
