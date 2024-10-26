from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__)

purchasers = {
    "Ya.Moroz-1983@yandex.ru": {
        "id": 1,
        "name": "John Doe",
        "purchases": [
            {
                "id": "1",
                "time": "1729686754",
                "items": [
                    {"name": "Хлопок", "count": 10.0, "price": 64.50},
                ],
                "date": "26.10.2024",
                "total_price": 402.99
            },
            {
                "id": "2",
                "time": "1729686755",
                "items": [
                    {"name": "Свинина", "count": 5.0, "price": 25.00}
                ],
                "date": "23.10.2024",
                "total_price": 85.00
            }, 
            {
                "id": "3",
                "time": "1729686754",
                "items": [
                    {"name": "Хлопок", "count": 15.0, "price": 64.50},
                ],
                "date": "26.10.2024",
                "total_price": 402.99
            },
                        {
                "id": "4",
                "time": "1729686755",
                "items": [
                    {"name": "Свинина", "count": 11.0, "price": 25.00}
                ],
                "date": "21.10.2024",
                "total_price": 85.00
            }, 
                        {
                "id": "5",
                "time": "1729686755",
                "items": [
                    {"name": "Свинина", "count": 2.0, "price": 25.00}
                ],
                "date": "20.10.2024",
                "total_price": 85.00
            }, 
        ]
    },
    "test@example.com": {
        "id": 2,
        "name": "Jane Smith",
        "purchases": []
    }
}

@api.route('/purchasers', methods=['GET'])
def get_purchaser():
    email = request.args.get('email')
    purchaser = purchasers.get(email)
    if purchaser:
        return jsonify(purchaser), 200
    return jsonify({"error": "Purchaser not found"}), 404

@api.route('/purchasers/<int:purchaser_id>/receipts', methods=['GET'])
def get_receipts(purchaser_id):
    from_time = request.args.get('from')
    to_time = request.args.get('to')
    purchaser = next((p for p in purchasers.values() if p["id"] == purchaser_id), None)
    if not purchaser:
        return jsonify({"error": "Purchaser not found"}), 404

    receipts = purchaser["purchases"]
    return jsonify(receipts), 200
