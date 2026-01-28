from flask import Flask , redirect , request , jsonify

app = Flask(__name__)

# To store details of Books

library = {

}


@app.route('/')
def home_page():
    return 'to kese hai app log '

# Add a book with id, title , author, year
@app.route("/addbooks",methods=['POST'])
def  add_book():
    if request.method == 'POST':
        data = request.get_json()

        required_field = ['id','title','author','year']
        for field  in required_field:
            if field not in data:
                return jsonify({"error":f"Missing field:{field}"})

        book_id = data['id']
        if book_id in library:
            return jsonify({"error":"Book with this ID is already Exist"})

        library[book_id] = data
        return jsonify({
            'message': "Book added successfully",
            "book" : data
        })

# Retrieve book details  
@app.route('/books/<int:book_id>' , methods=['GET'])
def get_book_details(book_id):
    if book_id not in library:
        return jsonify({"error":"Book not found"})
    
    try:
        return jsonify(library[book_id])
    except Exception as e :
        return f"Error:{e}"
    

# filter book by year 
@app.route("/books/search", methods=['GET'])
def book_search():
    year = request.args.get("year", type=int)

    if year is None:
        return jsonify({"error":"year is required"})
    
    result = [ book for book in library.values() if book["year"]== year ]
    return jsonify(result)

# Delete a book 
@app.route("/books/<int:book_id>",methods=['DELETE'])
def delete_book(book_id):
    if book_id not in library :
        return jsonify({'error':"Book not found"})
    
    del_book = library.pop(book_id)

    return jsonify({
        "message": "Book deleted successfully",
        "book": del_book
    })



if __name__ == "__main__":
    app.run(debug=True)