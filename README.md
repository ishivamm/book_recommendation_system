# 📚 Book Recommendation System

A **Machine Learning–based Book Recommendation System** that suggests books to users based on similarity and popularity.  
The project uses **data preprocessing, similarity metrics, and recommendation algorithms** to generate personalized book recommendations.

Live preview :https://bookrecommendationsystem-go5yrygmqyyzos5be6hjix.streamlit.app/
---

## 🚀 Project Overview

With thousands of books available online, it becomes difficult for users to find books that match their interests. This project solves that problem by building a **recommendation engine** that suggests books based on user preferences and historical data.

The system analyzes book ratings and similarities to recommend books that users are most likely to enjoy.

---

## 🎯 Features

- 📖 Top Books Display – Shows the most popular books based on ratings
- 🔎 Book-Based Recommendation – Suggests books similar to the selected book
- 🤖 Machine Learning Model – Uses similarity algorithms to generate recommendations
- 📊 Data Processing Pipeline – Cleans and processes the dataset
- ⚡ Fast Recommendation Engine – Uses precomputed similarity matrices

---

## 🧠 Recommendation Approach

The system uses **Collaborative Filtering and Similarity Metrics**.

### 1️⃣ Popularity-Based Recommendation
Recommends books with:
- High ratings
- Large number of reviews

### 2️⃣ Similarity-Based Recommendation
Uses **Cosine Similarity** to recommend books similar to a selected book.

Workflow:

```
User selects a book
        ↓
System finds similar books
        ↓
Top N similar books are recommended
```

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook
- Machine Learning

---

## 📂 Project Structure

```
book_recommendation_system
│
├── book_recommendation_system.ipynb
├── books.csv
├── ratings.csv
├── users.csv
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/ishivamm/book_recommendation_system.git
```

Navigate to the project directory:

```bash
cd book_recommendation_system
```

Install dependencies:

```bash
pip install pandas numpy scikit-learn matplotlib
```

---

## ▶️ How to Run

Open Jupyter Notebook:

```bash
jupyter notebook
```

Run the notebook:

```
book_recommendation_system.ipynb
```

Steps:
1. Load dataset  
2. Perform preprocessing  
3. Train recommendation model  
4. Generate recommendations  

---

## 📊 Dataset

The dataset contains:

- Books metadata
- User ratings
- User information

These datasets help train the recommendation model to predict similar books.

---

## 📸 Example Recommendation

Example output:

```
Input Book:
Harry Potter and the Sorcerer's Stone

Recommended Books:
1. Harry Potter and the Chamber of Secrets
2. Harry Potter and the Prisoner of Azkaban
3. Percy Jackson & The Olympians
4. The Hobbit
5. The Chronicles of Narnia
```

---

## 📈 Future Improvements

- Deploy using **Streamlit**
- Add **Deep Learning Recommender System**
- Add **User personalization**
- Improve recommendation accuracy with **Matrix Factorization**

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Submit a pull request

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Shivam Maurya**

GitHub: https://github.com/ishivamm
