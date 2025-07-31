# import os
# import json
# import requests
# from flask import Flask, request, jsonify, render_template
# from dotenv import load_dotenv
# from sentence_transformers import SentenceTransformer
# import chromadb
# from bs4 import BeautifulSoup

# # Load env vars
# load_dotenv()
# OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
# if not OPENROUTER_API_KEY:
#     raise ValueError("OPENROUTER_API_KEY not set in environment")

# # Setup ChromaDB client and collection
# client = chromadb.PersistentClient(path="./chroma_db")
# collection = client.get_or_create_collection(name="portfolio_rag_collection")

# # Load Sentence Transformer model
# embedder = SentenceTransformer("all-MiniLM-L6-v2")

# app = Flask(__name__, template_folder='templates')

# def get_about_me_text():
#     """Parse templates/index.html to extract About Me section text."""
#     with open("templates/index.html", "r", encoding="utf-8") as f:
#         soup = BeautifulSoup(f, "html.parser")
#     about_section = soup.find(id="about")
#     if not about_section:
#         return ""
#     # Extract visible text only, join paragraphs
#     paragraphs = about_section.find_all("p")
#     about_text = "\n".join(p.get_text(strip=True) for p in paragraphs)
#     return about_text

# def get_github_repos():
#     """Fetch public repos from GitHub API for user 'Anirudhpatil367'."""
#     url = "https://api.github.com/users/Anirudhpatil367/repos"
#     response = requests.get(url)
#     response.raise_for_status()
#     repos = response.json()
#     # Simplify and join repo names + descriptions
#     repo_texts = []
#     for repo in repos:
#         name = repo.get("name", "")
#         desc = repo.get("description", "")
#         repo_texts.append(f"{name}: {desc}")
#     return "\n".join(repo_texts)

# def add_documents_to_collection(texts):
#     """Add list of text chunks to Chroma vector DB with embeddings."""
#     for i, doc in enumerate(texts):
#         embedding = embedder.encode(doc).tolist()
#         collection.add(
#             documents=[doc],
#             ids=[f"doc_{i}"],
#             embeddings=[embedding]
#         )

# def prepare_vector_store():
#     """Load About Me and GitHub repos, split, embed and store if empty."""
#     if collection.count() > 0:
#         return  # Already populated

#     about_me = get_about_me_text()
#     github_data = get_github_repos()

#     combined_text = about_me + "\n\n" + github_data

#     # Split into ~500 char chunks for embedding
#     chunk_size = 500
#     chunks = [combined_text[i:i+chunk_size] for i in range(0, len(combined_text), chunk_size)]

#     add_documents_to_collection(chunks)
#     print("Vector store populated with About Me + GitHub data")

# def query_openrouter(prompt):
#     url = "https://openrouter.ai/api/v1/chat/completions"
#     headers = {
#         "Authorization": f"Bearer {OPENROUTER_API_KEY}",
#         "Content-Type": "application/json"
#     }
#     data = {
#         "model": "mistralai/mistral-7b-instruct:free",
#         "messages": [
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": prompt}
#         ]
#     }
#     response = requests.post(url, headers=headers, json=data)
#     response.raise_for_status()
#     result = response.json()
#     return result['choices'][0]['message']['content']

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/api/chat", methods=["POST"])
# def chat():
#     user_question = request.json.get("question", "")
#     if not user_question:
#         return jsonify({"error": "No question provided"}), 400

#     # Embed user question
#     q_embedding = embedder.encode(user_question).tolist()

#     # Retrieve top 3 docs from Chroma
#     results = collection.query(query_embeddings=[q_embedding], n_results=3)
#     docs = results['documents'][0]  # list of strings

#     # Join retrieved docs to create context
#     context = "\n".join(docs)

#     # Construct prompt telling model to ONLY use this context
#     prompt = (
#         f"You are a helpful assistant. Use ONLY the information in the context below to answer the question.\n\n"
#         f"Context:\n{context}\n\n"
#         f"Question: {user_question}\n"
#         f"Answer:"
#     )

#     try:
#         answer = query_openrouter(prompt)
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

#     return jsonify({"answer": answer})

# if __name__ == "__main__":
#     prepare_vector_store()
#     app.run(debug=True)

################this was working succesffully ###################
# import os
# import json
# import requests
# from flask import Flask, request, jsonify, render_template
# from dotenv import load_dotenv
# from sentence_transformers import SentenceTransformer
# import chromadb
# from bs4 import BeautifulSoup

# # Load env vars
# load_dotenv()
# OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
# if not OPENROUTER_API_KEY:
#     raise ValueError("OPENROUTER_API_KEY not set in environment")

# # Setup ChromaDB client and collection
# client = chromadb.PersistentClient(path="./chroma_db")
# collection = client.get_or_create_collection(name="portfolio_rag_collection")

# # Load Sentence Transformer model
# embedder = SentenceTransformer("all-MiniLM-L6-v2")

# app = Flask(__name__, template_folder='templates')


# def get_full_page_text():
#     """Extract all visible text from entire index.html page."""
#     with open("templates/index.html", "r", encoding="utf-8") as f:
#         soup = BeautifulSoup(f, "html.parser")

#     # Remove scripts, styles, noscript tags
#     for script_or_style in soup(["script", "style", "noscript"]):
#         script_or_style.decompose()

#     # Get all visible text with line breaks
#     text = soup.get_text(separator="\n")

#     # Clean empty lines and strip whitespace
#     lines = [line.strip() for line in text.splitlines()]
#     visible_lines = [line for line in lines if line]

#     full_text = "\n".join(visible_lines)
#     print(f"DEBUG: Extracted full page text length: {len(full_text)} characters")
#     return full_text


# def get_github_repos():
#     """Fetch public repos from GitHub API for user 'Anirudhpatil367'."""
#     url = "https://api.github.com/users/Anirudhpatil367/repos"
#     response = requests.get(url)
#     response.raise_for_status()
#     repos = response.json()
#     repo_texts = []
#     for repo in repos:
#         name = repo.get("name", "")
#         desc = repo.get("description", "")
#         repo_texts.append(f"{name}: {desc}")
#     return "\n".join(repo_texts)


# def add_documents_to_collection(texts):
#     """Add list of text chunks to Chroma vector DB with embeddings."""
#     for i, doc in enumerate(texts):
#         embedding = embedder.encode(doc).tolist()
#         collection.add(
#             documents=[doc],
#             ids=[f"doc_{i}"],
#             embeddings=[embedding]
#         )


# # def prepare_vector_store():
# #     """Load full page text and GitHub repos, split, embed, and store if empty."""
# #     if collection.count() > 0:
# #         print("Vector store already populated.")
# #         return

# #     full_page_text = get_full_page_text()
# #     github_data = get_github_repos()

# #     combined_text = full_page_text + "\n\n" + github_data

# #     chunk_size = 500
# #     chunks = [combined_text[i:i + chunk_size] for i in range(0, len(combined_text), chunk_size)]

# #     add_documents_to_collection(chunks)
# #     print("Vector store populated with full index.html content + GitHub data")
# def prepare_vector_store():
#     if collection.count() > 0:
#         print(f"Collection already has {collection.count()} documents")
#         return  # Already populated

#     about_me = get_about_me_text()
#     print("Extracted About Me text:", repr(about_me))  # DEBUG: see what's extracted

#     github_data = get_github_repos()
#     print("Extracted GitHub data:", repr(github_data))  # DEBUG

#     combined_text = about_me + "\n\n" + github_data

#     # Split into ~500 char chunks for embedding
#     chunk_size = 500
#     chunks = [combined_text[i:i+chunk_size] for i in range(0, len(combined_text), chunk_size)]
#     print(f"Split into {len(chunks)} chunks")

#     add_documents_to_collection(chunks)
#     print("Vector store populated with About Me + GitHub data")


# def query_openrouter(prompt):
#     url = "https://openrouter.ai/api/v1/chat/completions"
#     headers = {
#         "Authorization": f"Bearer {OPENROUTER_API_KEY}",
#         "Content-Type": "application/json"
#     }
#     data = {
#         "model": "mistralai/mistral-7b-instruct:free",
#         "messages": [
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": prompt}
#         ]
#     }
#     response = requests.post(url, headers=headers, json=data)
#     response.raise_for_status()
#     result = response.json()
#     return result['choices'][0]['message']['content']


# @app.route("/")
# def home():
#     return render_template("index.html")


# @app.route("/api/chat", methods=["POST"])
# def chat():
#     user_question = request.json.get("question", "")
#     if not user_question:
#         return jsonify({"error": "No question provided"}), 400

#     # Embed user question
#     q_embedding = embedder.encode(user_question).tolist()

#     # Retrieve top 3 docs from Chroma
#     results = collection.query(query_embeddings=[q_embedding], n_results=3)
#     docs = results['documents'][0]  # list of strings

#     # Join retrieved docs to create context
#     context = "\n".join(docs)

#     # Construct prompt telling model to ONLY use this context
#     prompt = (
#         f"You are a helpful assistant. Use ONLY the information in the context below to answer the question.\n\n"
#         f"Context:\n{context}\n\n"
#         f"Question: {user_question}\n"
#         f"Answer:"
#     )

#     try:
#         answer = query_openrouter(prompt)
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

#     return jsonify({"answer": answer})


# if __name__ == "__main__":
#     prepare_vector_store()
#     app.run(debug=True)

# import os
# import requests
# from flask import Flask, request, jsonify, send_from_directory
# from dotenv import load_dotenv
# from sentence_transformers import SentenceTransformer
# import chromadb
# from bs4 import BeautifulSoup

# # Load environment variables from .env
# load_dotenv()
# OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
# if not OPENROUTER_API_KEY:
#     raise ValueError("OPENROUTER_API_KEY not set in environment")

# # Setup ChromaDB client and collection
# client = chromadb.PersistentClient(path="./chroma_db")
# collection = client.get_or_create_collection(name="portfolio_rag_collection")

# # Load sentence transformer model
# embedder = SentenceTransformer("all-MiniLM-L6-v2")

# app = Flask(__name__, static_folder='templates', static_url_path='')


# def get_full_page_text():
#     """Extract all visible text and relevant attribute info (href, src) from index.html."""
#     with open("templates/index.html", "r", encoding="utf-8") as f:
#         soup = BeautifulSoup(f, "html.parser")

#     # Remove scripts, styles, noscript tags
#     for tag in soup(["script", "style", "noscript"]):
#         tag.decompose()

#     # Extract all visible text
#     texts = soup.stripped_strings
#     visible_text = "\n".join(texts)

#     # Additionally, extract attribute values from links, images, and common tags for more info
#     attrs_texts = []

#     # Collect href and title attributes from <a> tags (LinkedIn, Github, Email links)
#     for a_tag in soup.find_all("a"):
#         href = a_tag.get("href", "")
#         if href:
#             attrs_texts.append(f"Link: {href}")
#         title = a_tag.get("title", "")
#         if title:
#             attrs_texts.append(f"Link title: {title}")

#     # Collect src attributes from images
#     for img_tag in soup.find_all("img"):
#         src = img_tag.get("src", "")
#         alt = img_tag.get("alt", "")
#         if src:
#             attrs_texts.append(f"Image source: {src}")
#         if alt:
#             attrs_texts.append(f"Image alt: {alt}")

#     # You can add more tag attribute extractions here if needed

#     # Combine visible text and attributes text
#     combined_text = visible_text + "\n" + "\n".join(attrs_texts)

#     print(f"DEBUG: Extracted text length: {len(combined_text)} characters")
#     return combined_text


# def get_github_repos():
#     """Fetch public repos from GitHub API for user 'Anirudhpatil367'."""
#     url = "https://api.github.com/users/Anirudhpatil367/repos"
#     response = requests.get(url)
#     response.raise_for_status()
#     repos = response.json()
#     repo_texts = []
#     for repo in repos:
#         name = repo.get("name", "")
#         desc = repo.get("description", "")
#         repo_texts.append(f"{name}: {desc}")
#     return "\n".join(repo_texts)


# def add_documents_to_collection(texts):
#     """Add list of text chunks to Chroma vector DB with embeddings."""
#     for i, doc in enumerate(texts):
#         embedding = embedder.encode(doc).tolist()
#         collection.add(
#             documents=[doc],
#             ids=[f"doc_{i}"],
#             embeddings=[embedding]
#         )


# def prepare_vector_store():
#     if collection.count() > 0:
#         print(f"Collection already has {collection.count()} documents")
#         return  # Already populated

#     about_me = get_full_page_text()
#     print("Extracted About Me text (sample):", repr(about_me[:500]))  # Debug first 500 chars

#     github_data = get_github_repos()
#     print("Extracted GitHub data (sample):", repr(github_data[:500]))  # Debug first 500 chars

#     combined_text = about_me + "\n\n" + github_data

#     # Split into ~500 char chunks for embedding
#     chunk_size = 500
#     chunks = [combined_text[i:i+chunk_size] for i in range(0, len(combined_text), chunk_size)]
#     print(f"Split into {len(chunks)} chunks")

#     add_documents_to_collection(chunks)
#     print("Vector store populated with About Me + GitHub data")


# def query_openrouter(prompt):
#     url = "https://openrouter.ai/api/v1/chat/completions"
#     headers = {
#         "Authorization": f"Bearer {OPENROUTER_API_KEY}",
#         "Content-Type": "application/json"
#     }
#     data = {
#         "model": "mistralai/mistral-7b-instruct:free",
#         "messages": [
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": prompt}
#         ]
#     }
#     response = requests.post(url, headers=headers, json=data)
#     response.raise_for_status()
#     result = response.json()
#     return result['choices'][0]['message']['content']


# @app.route("/")
# def serve_index():
#     # Serve your index.html file
#     return send_from_directory(app.static_folder, "index.html")


# @app.route("/api/chat", methods=["POST"])
# def chat():
#     user_question = request.json.get("question", "")
#     if not user_question:
#         return jsonify({"error": "No question provided"}), 400

#     # Embed user question
#     q_embedding = embedder.encode(user_question).tolist()

#     # Retrieve top 3 docs from Chroma
#     results = collection.query(query_embeddings=[q_embedding], n_results=3)
#     docs = results['documents'][0]  # list of strings

#     # Join retrieved docs to create context
#     context = "\n".join(docs)

#     # Construct prompt telling model to ONLY use this context
#     prompt = (
#         f"You are a helpful assistant. Use ONLY the information in the context below to answer the question.\n\n"
#         f"Context:\n{context}\n\n"
#         f"Question: {user_question}\n"
#         f"Answer:"
#     )

#     try:
#         answer = query_openrouter(prompt)
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

#     return jsonify({"answer": answer})


# if __name__ == "__main__":
#     prepare_vector_store()
#     app.run(debug=True)

# import os
# import json
# import requests
# from flask import Flask, request, jsonify, render_template
# from dotenv import load_dotenv
# from sentence_transformers import SentenceTransformer
# import chromadb
# from bs4 import BeautifulSoup

# # Load environment variables
# load_dotenv()
# OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
# if not OPENROUTER_API_KEY:
#     raise ValueError("OPENROUTER_API_KEY not set in environment")

# # Setup ChromaDB client and collection
# client = chromadb.PersistentClient(path="./chroma_db")
# collection = client.get_or_create_collection(name="portfolio_rag_collection")

# # Load Sentence Transformer model
# embedder = SentenceTransformer("all-MiniLM-L6-v2")

# app = Flask(__name__, template_folder='templates')


# def extract_text_and_links_from_html():
#     """Extract all visible text AND all href links from index.html."""
#     with open("templates/index.html", "r", encoding="utf-8") as f:
#         soup = BeautifulSoup(f, "html.parser")

#     # Remove scripts, styles, noscript tags
#     for tag in soup(["script", "style", "noscript"]):
#         tag.decompose()

#     # Extract visible text
#     visible_text_lines = [line.strip() for line in soup.get_text(separator="\n").splitlines() if line.strip()]
#     visible_text = "\n".join(visible_text_lines)

#     # Extract all href links with their text for context
#     links = []
#     for a in soup.find_all("a", href=True):
#         href = a['href'].strip()
#         link_text = a.get_text(strip=True)
#         # Include link text + URL as one string for embedding
#         if link_text:
#             links.append(f"{link_text}: {href}")
#         else:
#             links.append(href)

#     links_text = "\n".join(links)

#     combined = visible_text + "\n\nLinks:\n" + links_text
#     print(f"DEBUG: Extracted visible text length: {len(visible_text)} chars")
#     print(f"DEBUG: Extracted links count: {len(links)}")
#     return combined


# def get_github_repos():
#     """Fetch public repos from GitHub API for user 'Anirudhpatil367'."""
#     url = "https://api.github.com/users/Anirudhpatil367/repos"
#     response = requests.get(url)
#     response.raise_for_status()
#     repos = response.json()
#     repo_texts = []
#     for repo in repos:
#         name = repo.get("name", "")
#         desc = repo.get("description", "")
#         repo_texts.append(f"{name}: {desc}")
#     return "\n".join(repo_texts)


# def add_documents_to_collection(text_chunks):
#     """Add list of text chunks to Chroma vector DB with embeddings."""
#     for i, doc in enumerate(text_chunks):
#         embedding = embedder.encode(doc).tolist()
#         collection.add(
#             documents=[doc],
#             ids=[f"doc_{i}"],
#             embeddings=[embedding]
#         )


# def prepare_vector_store():
#     if collection.count() > 0:
#         print(f"Collection already has {collection.count()} documents")
#         return  # Already populated

#     # Extract visible text + links from HTML
#     full_text = extract_text_and_links_from_html()
#     # Get GitHub repo info
#     github_text = get_github_repos()

#     combined_text = full_text + "\n\nGitHub Repos:\n" + github_text

#     # Split combined text into ~500 char chunks
#     chunk_size = 500
#     chunks = [combined_text[i:i + chunk_size] for i in range(0, len(combined_text), chunk_size)]

#     add_documents_to_collection(chunks)
#     print(f"Vector store populated with {len(chunks)} chunks")


# def query_openrouter(prompt):
#     url = "https://openrouter.ai/api/v1/chat/completions"
#     headers = {
#         "Authorization": f"Bearer {OPENROUTER_API_KEY}",
#         "Content-Type": "application/json"
#     }
#     data = {
#         "model": "mistralai/mistral-7b-instruct:free",
#         "messages": [
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": prompt}
#         ]
#     }
#     response = requests.post(url, headers=headers, json=data)
#     response.raise_for_status()
#     result = response.json()
#     return result['choices'][0]['message']['content']


# @app.route("/")
# def home():
#     return render_template("index.html")


# @app.route("/api/chat", methods=["POST"])
# def chat():
#     user_question = request.json.get("question", "").strip()
#     if not user_question:
#         return jsonify({"error": "No question provided"}), 400

#     # Embed user question
#     q_embedding = embedder.encode(user_question).tolist()

#     # Retrieve top 3 documents from Chroma
#     results = collection.query(query_embeddings=[q_embedding], n_results=3)
#     docs = results['documents'][0]

#     # Join retrieved docs to create context for LLM
#     context = "\n".join(docs)

#     # Construct prompt instructing the model to use ONLY context
#     prompt = (
#         f"You are a helpful assistant. Use ONLY the information in the context below to answer the question.\n\n"
#         f"Context:\n{context}\n\n"
#         f"Question: {user_question}\n"
#         f"Answer:"
#     )

#     try:
#         answer = query_openrouter(prompt)
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

#     return jsonify({"answer": answer})


# if __name__ == "__main__":
#     prepare_vector_store()
#     app.run(debug=True)


# ########except contact working everything for openrouter api ################
# import os
# import json
# import requests
# from flask import Flask, request, jsonify, render_template
# from dotenv import load_dotenv
# from sentence_transformers import SentenceTransformer
# import chromadb
# from bs4 import BeautifulSoup

# # Load environment variables
# load_dotenv()
# OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
# if not OPENROUTER_API_KEY:
#     raise ValueError("OPENROUTER_API_KEY not set in environment")

# # Setup ChromaDB client and collection
# client = chromadb.PersistentClient(path="./chroma_db")
# collection = client.get_or_create_collection(name="portfolio_rag_collection")

# # Load Sentence Transformer model
# embedder = SentenceTransformer("all-MiniLM-L6-v2")

# app = Flask(__name__, template_folder='templates')

# def extract_text_and_links_from_html():
#     with open("templates/index.html", "r", encoding="utf-8") as f:
#         soup = BeautifulSoup(f, "html.parser")

#     for tag in soup(["script", "style", "noscript"]):
#         tag.decompose()

#     visible_text_lines = [line.strip() for line in soup.get_text(separator="\n").splitlines() if line.strip()]
#     visible_text = "\n".join(visible_text_lines)

#     links = []
#     for a in soup.find_all("a", href=True):
#         href = a['href'].strip()
#         link_text = a.get_text(strip=True)
#         links.append(f"{link_text}: {href}" if link_text else href)

#     links_text = "\n".join(links)
#     combined = visible_text + "\n\nLinks:\n" + links_text
#     print(f"DEBUG: Extracted visible text length: {len(visible_text)} chars")
#     print(f"DEBUG: Extracted links count: {len(links)}")
#     return combined

# def get_work_experience_text():
#     with open("templates/index.html", "r", encoding="utf-8") as f:
#         soup = BeautifulSoup(f, "html.parser")

#     work_section = soup.find(id="work-experience")
#     if work_section:
#         for tag in work_section(["script", "style", "noscript"]):
#             tag.decompose()

#         work_text = work_section.get_text(separator="\n").strip()
#         lines = [line.strip() for line in work_text.splitlines()]
#         visible_lines = [line for line in lines if line]
#         work_text_clean = "\n".join(visible_lines)
#         print(f"DEBUG: Extracted Work Experience text length: {len(work_text_clean)} characters")
#         return work_text_clean
#     else:
#         print("DEBUG: No Work Experience section found.")
#         return ""

# def get_github_repos():
#     url = "https://api.github.com/users/Anirudhpatil367/repos"
#     response = requests.get(url)
#     response.raise_for_status()
#     repos = response.json()
#     repo_texts = []
#     for repo in repos:
#         name = repo.get("name", "")
#         desc = repo.get("description", "")
#         repo_texts.append(f"{name}: {desc}")
#     return "\n".join(repo_texts)

# def add_documents_to_collection(text_chunks):
#     for i, doc in enumerate(text_chunks):
#         embedding = embedder.encode(doc).tolist()
#         collection.add(
#             documents=[doc],
#             ids=[f"doc_{i}"],
#             embeddings=[embedding]
#         )

# def prepare_vector_store():
#     if collection.count() > 0:
#         print(f"Collection already has {collection.count()} documents")
#         return

#     full_text = extract_text_and_links_from_html()
#     work_text = get_work_experience_text()
#     github_text = get_github_repos()

#     combined_text = full_text + "\n\nWork Experience:\n" + work_text + "\n\nGitHub Repos:\n" + github_text

#     chunk_size = 500
#     chunks = [combined_text[i:i + chunk_size] for i in range(0, len(combined_text), chunk_size)]

#     add_documents_to_collection(chunks)
#     print(f"Vector store populated with {len(chunks)} chunks")

# def query_openrouter(prompt):
#     url = "https://openrouter.ai/api/v1/chat/completions"
#     headers = {
#         "Authorization": f"Bearer {OPENROUTER_API_KEY}",
#         "Content-Type": "application/json"
#     }
#     data = {
#         "model": "mistralai/mistral-7b-instruct:free",
#         "messages": [
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": prompt}
#         ]
#     }
#     response = requests.post(url, headers=headers, json=data)
#     response.raise_for_status()
#     result = response.json()
#     return result['choices'][0]['message']['content']

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/api/chat", methods=["POST"])
# def chat():
#     user_question = request.json.get("question", "").strip()
#     if not user_question:
#         return jsonify({"error": "No question provided"}), 400

#     q_embedding = embedder.encode(user_question).tolist()
#     results = collection.query(query_embeddings=[q_embedding], n_results=3)
#     docs = results['documents'][0]
#     context = "\n".join(docs)

#     prompt = (
#         f"You are a helpful assistant. Use ONLY the information in the context below to answer the question.\n\n"
#         f"Context:\n{context}\n\n"
#         f"Question: {user_question}\n"
#         f"Answer:"
#     )

#     try:
#         answer = query_openrouter(prompt)
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

#     return jsonify({"answer": answer})

# if __name__ == "__main__":
#     prepare_vector_store()
#     app.run(debug=True)

########except contact working everything ################
import os
import json
import requests
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import chromadb
from bs4 import BeautifulSoup
import google.generativeai as genai

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not set in environment")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
gemini_model = genai.GenerativeModel("gemini-1.5-flash")  # or "gemini-1.5-pro"

# Setup ChromaDB client and collection
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="portfolio_rag_collection")

# Load Sentence Transformer model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

app = Flask(__name__, template_folder='templates')

def extract_text_and_links_from_html():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    visible_text_lines = [line.strip() for line in soup.get_text(separator="\n").splitlines() if line.strip()]
    visible_text = "\n".join(visible_text_lines)

    links = []
    for a in soup.find_all("a", href=True):
        href = a['href'].strip()
        link_text = a.get_text(strip=True)
        links.append(f"{link_text}: {href}" if link_text else href)

    links_text = "\n".join(links)
    combined = visible_text + "\n\nLinks:\n" + links_text
    print(f"DEBUG: Extracted visible text length: {len(visible_text)} chars")
    print(f"DEBUG: Extracted links count: {len(links)}")
    return combined

def get_work_experience_text():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    work_section = soup.find(id="work-experience")
    if work_section:
        for tag in work_section(["script", "style", "noscript"]):
            tag.decompose()

        work_text = work_section.get_text(separator="\n").strip()
        lines = [line.strip() for line in work_text.splitlines()]
        visible_lines = [line for line in lines if line]
        work_text_clean = "\n".join(visible_lines)
        print(f"DEBUG: Extracted Work Experience text length: {len(work_text_clean)} characters")
        return work_text_clean
    else:
        print("DEBUG: No Work Experience section found.")
        return ""

def get_github_repos():
    url = "https://api.github.com/users/Anirudhpatil367/repos"
    response = requests.get(url)
    response.raise_for_status()
    repos = response.json()
    repo_texts = []
    for repo in repos:
        name = repo.get("name", "")
        desc = repo.get("description", "")
        repo_texts.append(f"{name}: {desc}")
    return "\n".join(repo_texts)

def add_documents_to_collection(text_chunks):
    for i, doc in enumerate(text_chunks):
        embedding = embedder.encode(doc).tolist()
        collection.add(
            documents=[doc],
            ids=[f"doc_{i}"],
            embeddings=[embedding]
        )

def prepare_vector_store():
    if collection.count() > 0:
        print(f"Collection already has {collection.count()} documents")
        return

    full_text = extract_text_and_links_from_html()
    work_text = get_work_experience_text()
    github_text = get_github_repos()

    combined_text = full_text + "\n\nWork Experience:\n" + work_text + "\n\nGitHub Repos:\n" + github_text

    chunk_size = 500
    chunks = [combined_text[i:i + chunk_size] for i in range(0, len(combined_text), chunk_size)]

    add_documents_to_collection(chunks)
    print(f"Vector store populated with {len(chunks)} chunks")

def query_gemini(prompt):
    try:
        response = gemini_model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Gemini API error: {e}")
        return "Sorry, there was an error processing your request."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    user_question = request.json.get("question", "").strip()
    if not user_question:
        return jsonify({"error": "No question provided"}), 400

    q_embedding = embedder.encode(user_question).tolist()
    results = collection.query(query_embeddings=[q_embedding], n_results=3)
    docs = results['documents'][0]
    context = "\n".join(docs)

    prompt = (
        f"You are a helpful assistant. Use ONLY the information in the context below to answer the question.\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {user_question}\n"
        f"Answer:"
    )

    try:
        answer = query_gemini(prompt)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"answer": answer})

if __name__ == "__main__":
    prepare_vector_store()
    app.run(debug=True)
