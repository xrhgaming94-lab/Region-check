from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

class AccInfoAPI:
    """Free Fire Account Info API Wrapper"""
    
    BASE_URL = "https://infoooooo-v6v5.vercel.app/accinfo"
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def get_account_info(self, uid: str):
        try:
            response = self.session.get(
                self.BASE_URL,
                params={'uid': uid},
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

ff_api = AccInfoAPI()

@app.route('/region', methods=['GET'])
def get_region_info():
    """Get nickname, region, and liked count for a UID"""
    uid = request.args.get('uid')
    
    if not uid:
        return jsonify({
            "nickname": "",
            "region": "",
            "liked": "",
            "uid": ""
        }), 400
    
    if not uid.isdigit():
        return jsonify({
            "nickname": "",
            "region": "",
            "liked": "",
            "uid": uid
        }), 400
    
    # Fetch data from external API
    data = ff_api.get_account_info(uid)
    
    if not data or 'basicInfo' not in data:
        return jsonify({
            "nickname": "",
            "region": "",
            "liked": "",
            "uid": uid
        }), 404
    
    # Extract exactly the fields you want
    basic_info = data.get('basicInfo', {})
    
    result = {
        "nickname": basic_info.get('nickname', ''),
        "region": basic_info.get('region', ''),
        "liked": str(basic_info.get('liked', '')),
        "uid": uid
    }
    
    return jsonify(result)

@app.route('/region/<uid>', methods=['GET'])
def get_region_info_path(uid):
    """Alternative URL pattern: /region/1868812498"""
    return get_region_info()

@app.route('/accinfo', methods=['GET'])
def get_full_info():
    """Get complete account information"""
    uid = request.args.get('uid')
    
    if not uid:
        return jsonify({'error': 'UID required'}), 400
    
    data = ff_api.get_account_info(uid)
    
    if not data:
        return jsonify({'error': 'Data not found'}), 404
    
    return jsonify(data)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "nickname": "",
        "region": "",
        "liked": "",
        "uid": ""
    }), 404

if __name__ == '__main__':
    print("=" * 50)
    print("Free Fire Account Info API")
    print("=" * 50)
    print("\nServer running on: http://localhost:5000")
    print("\nUsage:")
    print("  http://localhost:5000/region?uid=1868812498")
    print("  or")
    print("  http://localhost:5000/region/1868812498")
    print("\nResponse format:")
    print('  {"nickname": "RAM┋ＶＲＡＪ", "region": "IND", "liked": "41216", "uid": "1868812498"}')
    print("\n" + "=" * 50)
    
    app.run(debug=True, host='0.0.0.0', port=5000)