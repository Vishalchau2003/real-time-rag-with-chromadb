
import os
import time
import chromadb

# Debugging print to check if script starts
print("🚀 ingest.py has started running...")

# Initialize ChromaDB
chroma_client = chromadb.PersistentClient(path="./vector_db")
collection = chroma_client.get_or_create_collection(name="documents")

# Folder to watch for new files
FOLDER_PATH = "data"
processed_files = set()  # Stores files that have already been processed

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
    """ Continuously watches the 'data' folder, ingests new files, and removes deleted files """
    print("📂 Watching folder:", os.path.abspath(FOLDER_PATH))

    while True:
        print("🔄 Entering the file-watching loop...")  # Debug print
        
        current_files = set(os.listdir(FOLDER_PATH))  # Get the latest list of files

        # 🔥 Detect NEW files
        for file in current_files:
            file_path = os.path.join(FOLDER_PATH, file)

            if file not in processed_files and os.path.exists(file_path):
                file_size = os.path.getsize(file_path)
                print(f"📝 Detected {file} with size: {file_size} bytes")

                if file_size > 0:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read().strip()

                    print(f"📝 Content of {file}: '{content}'")

                    if content:
                        collection.upsert(ids=[file], documents=[content])  # Store in ChromaDB
                        print(f"✅ Stored in ChromaDB: {file}")
                        print_stored_documents()
                        processed_files.add(file)  # Mark as processed
                    else:
                        print(f"⚠️ Skipped {file} (content empty after stripping)")
                else:
                    print(f"⚠️ Skipped {file} (file size is 0)")

        # 🔥 Detect DELETED files and REMOVE them from ChromaDB
        deleted_files = processed_files - current_files  # Find files that were removed
        for file in deleted_files:
            print(f"❌ File deleted: {file} - Removing from ChromaDB...")
            collection.delete(ids=[file])  # Remove from ChromaDB
            processed_files.remove(file)  # Remove from processed list
            print_stored_documents()  # Show updated stored documents

        print("⏳ Waiting for next check...\n")  # Debug print
        time.sleep(5)  # Check every 5 seconds


if __name__ == "__main__":
    watch_folder()
