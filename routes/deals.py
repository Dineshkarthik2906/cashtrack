from flask import Blueprint, request, jsonify
from database import get_db

deals_bp = Blueprint('deals', __name__)

@deals_bp.route('/deals', methods=['GET'])
def get_deals():
    conn = get_db()
    deals = conn.execute('SELECT * FROM deals ORDER BY created_at DESC').fetchall()
    conn.close()
    return jsonify([dict(d) for d in deals])

@deals_bp.route('/deals', methods=['POST'])
def add_deal():
    data = request.get_json()
    conn = get_db()
    conn.execute(
        'INSERT INTO deals (store, cashback_percent, original_price, deal_url) VALUES (?, ?, ?, ?)',
        (data['store'], data['cashback_percent'], data['original_price'], data.get('deal_url', ''))
    )
    conn.commit()
    conn.close()
    return jsonify({'message': 'Deal added'}), 201

@deals_bp.route('/deals/<int:id>', methods=['PUT'])
def redeem_deal(id):
    conn = get_db()
    conn.execute('UPDATE deals SET redeemed = 1 WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Deal redeemed'})

@deals_bp.route('/deals/<int:id>', methods=['DELETE'])
def delete_deal(id):
    conn = get_db()
    conn.execute('DELETE FROM deals WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Deal deleted'})

@deals_bp.route('/deals/stats', methods=['GET'])
def get_stats():
    conn = get_db()
    deals = conn.execute('SELECT * FROM deals WHERE redeemed = 1').fetchall()
    conn.close()
    total_saved = sum(d['original_price'] * d['cashback_percent'] / 100 for d in deals)
    return jsonify({'total_deals_redeemed': len(deals), 'total_saved': round(total_saved, 2)})
