from google.cloud import firestore

def get_db():
    return firestore.Client(
        project="solvox-ai-007",
        database="lumiverse-solution"
    )
