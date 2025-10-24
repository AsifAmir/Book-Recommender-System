## 📚 Book Recommender System

A **Flask-based web application** that recommends books to users using **collaborative filtering** and **cosine similarity**.  
This project helps readers discover new books similar to their favorites by analyzing user rating patterns.

🔗 **Live Demo:** [https://book-recommender-system-062.onrender.com](https://book-recommender-system-062.onrender.com)

---

### 🎯 Purpose

The goal of this project is to build a simple, intelligent system that mimics how online platforms like Goodreads or Amazon recommend books.  
It uses collaborative filtering to find books with similar audience preferences and provides an interactive, visually appealing web interface.  
📘 **Learning project for collaborative filtering and Flask deployment.**

---

### ⚙️ How It Works

1. **Data Preprocessing**
   - Loaded datasets containing book information, user ratings, and popularity metrics.
   - Cleaned and merged the data using Pandas.
   - Calculated average ratings and total votes for each book.

2. **Collaborative Filtering Model**
   - Created a **pivot table** (books × users) of ratings.
   - Computed **cosine similarity** between books based on user rating vectors.
   - Stored precomputed similarity matrices as `.pkl` files for efficient loading.

3. **Recommendation Logic**
   - When a user searches for a book, the system retrieves the most similar books using cosine similarity scores.
   - The homepage displays the **Top 50 most popular books**, ranked by average rating and vote count.

4. **Flask Web Integration**
   - Backend: Flask loads and serves the preprocessed data dynamically.
   - Frontend: HTML and Bootstrap used for responsive and clean UI design.
   - Users can view details like cover image, author, rating, and vote count.

---

### 🌟 Features

- 📖 Displays **Top 50 popular books** with details (cover, author, rating, votes)
- 🔍 **Search for a book** and receive similar recommendations
- ⚡ Fast performance using pre-saved pickle data
- 🧭 Clean, responsive interface built with Bootstrap
- ☁️ Ready for deployment on **Render**, **Heroku**, or any Flask-compatible host

---

### 🧰 Tech Stack

- **Language:** Python  
- **Libraries:** Pandas, NumPy, scikit-learn, Missingno  
- **Framework:** Flask  
- **Frontend:** HTML, CSS, Bootstrap  
- **Deployment:** Render  

---

### 🧩 Dataset

The project uses the **Book Recommendation Dataset** from Kaggle, containing information about books, user ratings, and book details.

📂 **Dataset Source:** [Book Recommendation Dataset – Kaggle](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset/data)

---

### 🧩 Limitations

- Recommendations are purely based on **user rating similarity** — no NLP or content-based analysis.  
- Cannot handle **cold-start problem** (new users or new books).  
- No **real-time feedback mechanism** for improving results dynamically.  
- Lacks **deep learning** or **semantic understanding** of books (future enhancement area).

---

### 🚀 How to Run Locally

1. **Clone this repository**
   ```bash
   git clone https://github.com/asifamir07/book-recommender-system.git
   cd book-recommender-system
