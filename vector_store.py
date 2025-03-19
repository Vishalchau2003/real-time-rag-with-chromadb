import chromadb

# Initialize ChromaDB
chroma_client = chromadb.PersistentClient(path="./vector_db")
collection = chroma_client.get_or_create_collection(name="documents")

def search(query):
    """Searches ChromaDB and returns relevant documents"""
    results = collection.query(query_texts=[query], n_results=3)
    return results["documents"]

if __name__ == "__main__":
    print("\n📂 Stored Documents in ChromaDB:")
    stored_docs = collection.get()
    
    if stored_docs["documents"]:
        for idx, doc in enumerate(stored_docs["documents"], start=1):
            print(f"{idx}. {doc}")
    else:
        print("❌ No documents found in the database.")

    query = input("\nEnter your search query: ")
    results = search(query)

    if results:
        print("\n🔎 Search Results:")
        for idx, doc in enumerate(results[0], start=1):
            print(f"{idx}. {doc}")
    else:
        print("\n❌ No relevant documents found.")
