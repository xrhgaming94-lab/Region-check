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
        "Cookie": "source=mb; region=PK; mspid2=13c49fb51ece78886ebf7108a4907756; _fbp=fb.1.1753985808817.794945392376454660; language=en; datadome=WQaG3HalUB3PsGoSXY3TdcrSQextsSFwkOp1cqZtJ7Ax4YkiERHUgkgHlEAIccQO~w8dzTGM70D9SzaH7vymmEqOrVeX5pIsPVE22Uf3TDu6W3WG7j36ulnTg2DltRO7; session_key=hq02g63z3zjcumm76mafcooitj7nc79y",
    }

    ________ = {
        "app_id": 100067,
        "login_id": str(______)
    }

    try:
        _________ = requests.post("https://topup.pk/api/auth/player_id_login", headers=_______, json=________, timeout=15)
        __________ = _________.json() if _________.text else {}
    except:
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

if __name__ == '__main__':
    _.run(host='0.0.0.0', port=5000)

def handler(___________, ____________):
    with _.test_client() as _____________:
        return _____________.open(
            path=___________.path,
            method=___________.method,
            headers=___________.headers,
            data=___________.get_data(),
            query_string=___________.query_string
        )