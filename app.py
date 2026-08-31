from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/region', methods=['GET'])
def region():
    uid = request.args.get('uid')
    
    # Default response structure
    response_data = {
        "credits": {
            "api_channel": "t.me/STAR_APIS",
            "developer": "t.me/STAR_GMR",
            "main_channel": "t.me/STAR_METHODE"
        },
        "nickname": "",
        "region": "",
        "liked": "",
        "uid": uid or ""
    }
    
    # Agar UID nahi hai to empty response do
    if not uid or not uid.isdigit():
        return jsonify(response_data)
    
    try:
        # Fetch from external API
        api_url = f"https://infoooooo-v6v5.vercel.app/accinfo?uid={uid}"
        resp = requests.get(api_url, timeout=10)
        
        if resp.status_code == 200:
            data = resp.json()
            basic = data.get('basicInfo', {})
            
            # Fill the data
            response_data["nickname"] = basic.get('nickname', '')
            response_data["region"] = basic.get('region', '')
            response_data["liked"] = str(basic.get('liked', ''))
            response_data["uid"] = uid
            
        return jsonify(response_data)
        
    except Exception as e:
        return jsonify(response_data)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "endpoint": "/region?uid=YOUR_UID",
        "example": "/region?uid=1868812498",
        "credits": {
            "api_channel": "t.me/STAR_APIS",
            "developer": "t.me/STAR_GMR",
            "main_channel": "t.me/STAR_METHODE"
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)