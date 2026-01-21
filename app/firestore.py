from google.cloud import firestore

def get_db(database: str = "(default)"):
    return firestore.Client(
        project="solvox-ai-007",
        database=database
    )
