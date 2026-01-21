from google.cloud import firestore

def get_db():
    return firestore.Client(
        project="YOUR_PROJECT_ID",
        database="lumiverse-solution"
    )
