from flask import Flask, jsonify, request
import random

app = Flask(__name__)

quotes = [
    {"id": 1, "text": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"id": 2, "text": "Code is like humor. When you have to explain it, it's bad.", "author": "Cory House"},
    {"id": 3, "text": "First, solve the problem. Then, write the code.", "author": "John Johnson"},
    {"id": 4, "text": "Simplicity is the soul of efficiency.", "author": "Austin Freeman"},
    {"id": 5, "text": "Fix the cause, not the symptom.", "author": "Steve Maguire"},
]

next_id = 6  # For generating new IDs

# TODO 1: Create GET /api/quote - return a random quote as JSON
@app.route('/api/quote',methods=['GET'])
def random_quote():
    return jsonify(random.choice(quotes))

# TODO 2: Create GET /api/quotes - return all quotes as JSON
@app.route('/api/quotes',methods=['GET'])
def all_quotes():
    return jsonify(quotes)

# TODO 3: Create POST /api/quotes - add a new quote
#   - Get JSON data from request.json
#   - Create new quote with next_id, text, and author
#   - Append to quotes list
#   - Increment next_id
#   - Return the new quote with status 201
@app.route('/api/quotes',methods=['POST'])
def add_quote():
    global next_id
    data = request.json
    new_quote={"id":next_id,"text":data['text'],"author":data['author']}
    quotes.append(new_quote)
    next_id+=1
    return jsonify(new_quote),201


# TODO 4: Create PUT /api/quotes/<id> - update a quote by id
#   - Get JSON data from request.json
#   - Find quote with matching id
#   - Update text and/or author
#   - Return the updated quote
#   - If not found, return error with status 404
@app.route('/api/quotes/<int:id>',methods=['PUT'])
def update_quote(id):
    data = request.json
    for quote in quotes:
        if quote['id']==id:
            if "text" in data:
                quote['text']=data['text']
            if "author" in data:
                quote['author']=data['author']
            return jsonify(quote)
    return jsonify({"error":"Quote not found"}),404

# TODO 5: Create DELETE /api/quotes/<id> - delete a quote by id
#   - Find and remove quote with matching id
#   - Return success message
#   - If not found, return error with status 404
@app.route('/api/quotes/<int:id>',methods=['DELETE'])
def delete_quote(id):
    for quote in quotes:
        if quote['id']==id:
            quotes.remove(quote)
            return jsonify({"message":"Quote deleted successfully"})
    return jsonify({"error":"Quote not found"}),404

if __name__ == "__main__":
    app.run(debug=True, port=5000)