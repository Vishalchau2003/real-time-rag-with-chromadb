import os
import time
import chromadb

# Initialize ChromaDB
chroma_client = chromadb.PersistentClient(path="./vector_db")
collection = chromadb.PersistentClient(path="./vector_db").get_or_create_collection(name="documents")

# Folder to watch for new files
FOLDER_PATH = "data"

def print_stored_documents():
    """ Prints all documents stored in ChromaDB """
    stored_data = collection.get()
    print("\n🔍 Raw Data from ChromaDB:", stored_data)
    if stored_data.get("documents"):
        print("\n📂 Stored Documents in ChromaDB:")
        for idx, doc in enumerate(stored_data["documents"], start=1):
            print(f"{idx}. {doc if doc else '[EMPTY DOCUMENT]'}")
    else:
        print("\n❌ No documents stored in ChromaDB.")

def watch_folder():
    """ Watches the 'data' folder and ingests new text files into ChromaDB with debugging info """
    existing_files = set(os.listdir(FOLDER_PATH))
    print("📂 Watching folder:", os.path.abspath(FOLDER_PATH))

    while True:
        current_files = set(os.listdir(FOLDER_PATH))
        new_files = current_files - existing_files  # Detect new files

        for file in new_files:
            file_path = os.path.join(FOLDER_PATH, file)
            
            # Check if file exists
            if os.path.exists(file_path):
                file_size = os.path.getsize(file_path)
                print(f"📝 Detected {file} with size: {file_size} bytes")
                
                if file_size > 0:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read().strip()  # Remove extra whitespace
                    print(f"📝 Content of {file}: '{content}'")
                    
                    if content:
                        collection.upsert(ids=[file], documents=[content])
                        print(f"✅ Stored in ChromaDB: {file}")
                        print_stored_documents()
                    else:
                        print(f"⚠️ Skipped {file} (content empty after stripping)")
                else:
                    print(f"⚠️ Skipped {file} (file size is 0)")
            else:
                print(f"⚠️ Skipped {file} (file does not exist)")
        
        existing_files = current_files  # Update file list
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    watch_folder()
