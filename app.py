from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy clothing data for demonstration
clothing_data = [
    {"name": "T-shirt", "style": "Casual", "size": "M", "occasion": "Everyday", "price": "$20"},
    {"name": "Dress Shirt", "style": "Formal", "size": "L", "occasion": "Office", "price": "$40"},
    {"name": "Jeans", "style": "Casual", "size": "M", "occasion": "Everyday", "price": "$30"},
    {"name": "Blazer", "style": "Formal", "size": "L", "occasion": "Office", "price": "$60"},
    {"name": "Dress", "style": "Formal", "size": "M", "occasion": "Party", "price": "$50"},
]

@app.route("/recommendations", methods=["POST"])
def get_recommendations():
    data = request.json
    style = data.get("style")
    size = data.get("size")
    occasion = data.get("occasion")

    recommendations = filter_clothing(style, size, occasion)
    return jsonify(recommendations)

def filter_clothing(style, size, occasion):
    filtered_items = []
    for item in clothing_data:
        if item["style"] == style and item["size"] == size and item["occasion"] == occasion:
            filtered_items.append(item)
    return filtered_items

if __name__ == "__main__":
    app.run(debug=True)
