import base64
import requests
from flask import Flask, request, jsonify

_ = Flask(__name__)

# Updated Hidden Links (Base64)
__ = "dC5tZS9TVEFSX01FVEhPREU="             
___ = "dC5tZS9TVEFSX01FVEhPREU="        
____ = "dC5tZS9TVEFSX0dNUg=="       

@_.route('/region', methods=['GET'])
def _____():
    ______ = request.args.get('uid')
    if not ______:
        return jsonify({"error": "uid required"}), 400

    _______ = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-MM,en-US;q=0.9,en;q=0.8",
        "Content-Type": "application/json",
        "Origin": "https://topup.pk",
        "Referer": "https://topup.pk/",
        "sec-ch-ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Android WebView";v="138"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Linux; Android 15; RMX5070 Build/UKQ1.231108.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.7204.157 Mobile Safari/537.36",
        "X-Requested-With": "mark.via.gp",
        "Cookie": "session_key=nc0gnuzm5msiyuxnn5mlwkrxpnizen3p;region=PK;source=mb;_fbp=fb.1.1772607670314.265654977791660607;_ga=GA1.1.1968215565.1772607669;_ga_C956TFJLD0=GS2.1.s1772607668$o1$g1$t1772607698$j30$l0$h0;datadome=pZPKg0pAoNyJc3k5Z4tuDnQtvcuZ~x86gN9Pm_73GNQQx9nIZC0QZUR3YpRpi31p6mi9nQ~NQiuUPrXJ0d1eAzPVRu8QJcF9LcjqTUYBVaHprHeFP2KOg9lnmvd0Q3LZ;language=en;mspid2=500b9a3b5640bb6a3b753b5f32a65f87",
    }

    ________ = {
        "app_id": 100067,
        "login_id": str(______)
    }

    try:
        _________ = requests.post("https://topup.pk/api/auth/player_id_login", headers=_______, json=________, timeout=15)
        __________ = _________.json() if _________.text else {}
    except Exception:
        __________ = {}

    return jsonify({
        "uid": ______,
        "nickname": __________.get('nickname', ''),
        "region": __________.get('region', ''),
        "credits": {
            "developer": base64.b64decode(__).decode('utf-8'),
            "main_channel": base64.b64decode(___).decode('utf-8'),
            "api_channel": base64.b64decode(____).decode('utf-8')
        }
    })

# Local development
if __name__ == '__main__':
    _.run(host='0.0.0.0', port=5000)

# Vercel entry point – keep the original '_' and also expose it as 'app'
app = _