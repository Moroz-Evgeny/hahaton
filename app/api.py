from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__)

purchasers = {
		"example@example.ru": {
			"id": 1,
			"name": "John Doe",
			"purchases": [
				{
					"id": "1",
					"time": "1729686754",
					"items": [{ "name": "Хлопок", "count": 10.0, "price": 64.5 }],
					"date": "21.10.2024",
					"total_price": 402.99
				},
				{
					"id": "2",
					"time": "1729686755",
					"items": [{ "name": "Свинина", "count": 5.0, "price": 25.0 }],
					"date": "20.10.2024",
					"total_price": 85.0
				},
				{
					"id": "3",
					"time": "1729686754",
					"items": [{ "name": "Хлопок", "count": 15.0, "price": 64.5 }],
					"date": "22.10.2024",
					"total_price": 402.99
				},
				{
					"id": "4",
					"time": "1729686755",
					"items": [{ "name": "Свинина", "count": 11.0, "price": 25.0 }],
					"date": "23.10.2024",
					"total_price": 85.0
				},
				{
					"id": "5",
					"time": "1729686755",
					"items": [{ "name": "Свинина", "count": 2.0, "price": 25.0 }],
					"date": "24.10.2024",
					"total_price": 85.0
				}
			]
		},
		"example2@example2.ru": {
			"id": 2,
			"name": "John Doe2",
			"purchases": [
				{
					"id": "1",
					"time": "1729686754",
					"items": [
						{ "name": "Хлопок", "count": 10.0, "price": 64.5 },
						{ "name": "Сыр", "count": 5.0, "price": 64.5 }
					],
					"date": "21.10.2024",
					"total_price": 402.99
				},
				{
					"id": "2",
					"time": "1729686755",
					"items": [{ "name": "Свинина", "count": 7.0, "price": 25.0 }],
					"date": "20.10.2024",
					"total_price": 85.0
				},
				{
					"id": "3",
					"time": "1729686754",
					"items": [{ "name": "Хлопок", "count": 17.0, "price": 64.5 }],
					"date": "22.10.2024",
					"total_price": 402.99
				},
				{
					"id": "4",
					"time": "1729686755",
					"items": [{ "name": "Свинина", "count": 8.0, "price": 25.0 }],
					"date": "23.10.2024",
					"total_price": 85.0
				},
				{
					"id": "5",
					"time": "1729686755",
					"items": [{ "name": "Свинина", "count": 2.0, "price": 25.0 }],
					"date": "24.10.2024",
					"total_price": 85.0
				}
			]
		},
        "example3@example3.ru": {
			"id": 3,
			"name": "John Doe3",
			"purchases": [
				{
					"id": "1",
					"time": "1729686754",
					"items": [
						{ "name": "Хлопок", "count": 12.0, "price": 64.5 },
						{ "name": "Сыр", "count": 5.0, "price": 64.5 }
					],
					"date": "21.10.2024",
					"total_price": 402.99
				},
				{
					"id": "2",
					"time": "1729686755",
					"items": [{ "name": "Свинина", "count": 5.0, "price": 25.0 }],
					"date": "20.10.2024",
					"total_price": 85.0
				},
				{
					"id": "3",
					"time": "1729686754",
					"items": [{ "name": "Хлопок", "count": 14.0, "price": 64.5 }],
					"date": "22.10.2024",
					"total_price": 402.99
				},
				{
					"id": "4",
					"time": "1729686755",
					"items": [{ "name": "Свинина", "count": 5.0, "price": 25.0 }],
					"date": "23.10.2024",
					"total_price": 85.0
				},
				{
					"id": "5",
					"time": "1729686755",
					"items": [{ "name": "Свинина", "count": 5.0, "price": 25.0 }],
					"date": "24.10.2024",
					"total_price": 85.0
				}
			]
		},
		"example4@example4.ru": {
			"id": 4,
			"name": "John Doe4",
			"purchases": [
				{
					"id": "1",
					"time": "1729686754",
					"items": [
						{ "name": "Хлопок", "count": 11.0, "price": 64.5 },
						{ "name": "Сыр", "count": 1.0, "price": 64.5 }
					],
					"date": "21.10.2024",
					"total_price": 402.99
				},
				{
					"id": "2",
					"time": "1729686755",
					"items": [{ "name": "Свинина", "count": 3.0, "price": 25.0 }],
					"date": "20.10.2024",
					"total_price": 85.0
				},
				{
					"id": "3",
					"time": "1729686754",
					"items": [{ "name": "Хлопок", "count": 2.0, "price": 64.5 }],
					"date": "22.10.2024",
					"total_price": 402.99
				},
				{
					"id": "4",
					"time": "1729686755",
					"items": [{ "name": "Свинина", "count": 25.0, "price": 25.0 }],
					"date": "23.10.2024",
					"total_price": 85.0
				},
				{
					"id": "5",
					"time": "1729686755",
					"items": [{ "name": "Свинина", "count": 17.0, "price": 25.0 }],
					"date": "24.10.2024",
					"total_price": 85.0
				}
			]
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
