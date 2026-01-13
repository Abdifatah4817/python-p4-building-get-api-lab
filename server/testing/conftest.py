from flask import Flask, jsonify
from models import db, Bakery, BakedGood

app = Flask(__name__)

# ✅ REQUIRED for CodeGrade
app.config.from_object('config.Config')
db.init_app(app)

# -------------------------------------
# GET /bakeries
# -------------------------------------
@app.route('/bakeries', methods=['GET'])
def get_bakeries():
    bakeries = Bakery.query.all()
    return jsonify([
        bakery.to_dict(rules=('baked_goods',))
        for bakery in bakeries
    ]), 200


# -------------------------------------
# GET /bakeries/<id>
# -------------------------------------
@app.route('/bakeries/<int:id>', methods=['GET'])
def get_bakery_by_id(id):
    bakery = Bakery.query.get(id)

    if not bakery:
        return jsonify({"error": "Bakery not found"}), 404

    return jsonify(
        bakery.to_dict(rules=('baked_goods',))
    ), 200


# -------------------------------------
# GET /baked_goods/by_price
# -------------------------------------
@app.route('/baked_goods/by_price', methods=['GET'])
def baked_goods_by_price():
    baked_goods = BakedGood.query.order_by(
        BakedGood.price.desc()
    ).all()

    return jsonify([
        good.to_dict(rules=('bakery',))
        for good in baked_goods
    ]), 200


# -------------------------------------
# GET /baked_goods/most_expensive
# -------------------------------------
@app.route('/baked_goods/most_expensive', methods=['GET'])
def most_expensive_baked_good():
    baked_good = BakedGood.query.order_by(
        BakedGood.price.desc()
    ).first()

    return jsonify(
        baked_good.to_dict(rules=('bakery',))
    ), 200
