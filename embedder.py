# embedder.py
import json
from sentence_transformers import SentenceTransformer
from chromadb.config import Settings
import chromadb
from examples import examples

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="./chroma_store")
collection = client.get_or_create_collection("testgen")

# Embed and store
# def store_examples():
#     for ex in examples:
#         embedding = model.encode(ex["spec"]).tolist()
#         collection.add(
#             documents=[ex["spec"]],
#             embeddings=[embedding],
#             metadatas=[{
#                 "id": ex["id"],
#                 "solution": ex["solution"],
#                 "test_code": ex["test_code"]
#             }],
#             ids=[ex["id"]]
#         )

def store_examples():
    for ex in examples:
        embedding = model.encode(ex["spec"]).tolist()
        print(f"📦 Storing example: {ex['id']}")
        collection.add(
            documents=[ex["spec"]],
            embeddings=[embedding],
            metadatas=[{
                "id": ex["id"],
                "solution": ex["solution"],
                "test_code": ex["test_code"]
            }],
            ids=[ex["id"]]
        )

def inspect_collection():
    results = collection.get(include=["documents", "metadatas"])
    print("📚 Collection contents:")
    for doc, meta in zip(results["documents"], results["metadatas"]):
        print(f"- Spec: {doc}")
        print(f"  ➤ ID: {meta['id']}")
        print(f"  ➤ Solution (truncated): {meta['solution'][:40]}...")
        print()

# # Retrieve closest match
# def retrieve_similar_examples(spec, top_k=1):
#     embedding = model.encode(spec).tolist()
#     results = collection.query(query_embeddings=[embedding], n_results=top_k)
#     print(json.dumps(results['metadatas'], indent=2))
#     return results['metadatas'][0]

def retrieve_similar_examples(spec, top_k=1):
    embedding = model.encode(spec).tolist()
    results = collection.query(query_embeddings=[embedding], n_results=top_k)

    print("🔍 Raw metadata results:")
    print(json.dumps(results['metadatas'], indent=2))

    if not results["metadatas"] or not results["metadatas"][0]:
        print("❌ No match found in ChromaDB.")
        return None

    best_match = results["metadatas"][0][0]
    print(f"✅ Best match: {best_match['id']}")
    return best_match

if __name__ == "__main__":
    store_examples()
    # inspect_collection()
    # retrieve_similar_examples("write a function add(a, b) that returns the sum of both numbers")
