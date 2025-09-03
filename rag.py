import chromadb

client = chromadb.PersistentClient(path="./db")
collection = client.get_collection(name="my_collection")

results = collection.query(
    query_texts=["What are some easy classes at Berkeley?"],
    n_results=10
)

print(results["documents"])