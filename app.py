from flask import Flask, render_template, request
import pickle

# Load data
popular_df = pickle.load(open('popular_df.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_score = pickle.load(open('similarity_matrix.pkl', 'rb'))

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html',
        book_name=list(popular_df['Book-Title'].values),
        author=list(popular_df['Book-Author'].values),
        image=list(popular_df['Image-URL-M'].values),
        votes=list(popular_df['num_ratings'].values),
        rating=list(popular_df['avg_ratings'].values)
    )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')

    # Check if the book exists
    if user_input not in pt.index:
        return render_template('recommend.html', error=f"No results found for '{user_input}'")

    # Find index of the given book
    index = pt.index.get_loc(user_input)

    # Get similarity scores
    similar_items = sorted(
        list(enumerate(similarity_score[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:6]  # Skip the book itself, take top 5

    # Collect details for the recommended books
    data = []
    for i in similar_items:
        book_title = pt.index[i[0]]
        temp_df = books[books['Book-Title'] == book_title]
        data.append({
            'title': temp_df['Book-Title'].values[0],
            'author': temp_df['Book-Author'].values[0],
            'image': temp_df['Image-URL-M'].values[0]
        })

    return render_template('recommend.html', data=data, user_input=user_input)


if __name__ == '__main__':
    app.run(debug=True)
