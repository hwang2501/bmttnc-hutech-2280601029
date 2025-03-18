from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher 
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON data"}), 400
        text = data['plain_text']  # Lấy văn bản cần mã hóa từ request
        key = int(data['key'])     # Số bước dịch chữ cái (vd: A->B là 1 bước)
        return jsonify({'encrypted_message': caesar_cipher.encrypt_text(text, key)})
    except KeyError as e:
        return jsonify({"error": f"Missing required key: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON data"}), 400
        text = data['cipher_text'] # Lấy văn bản mã hóa từ request
        key = int(data['key'])     # Dùng lại số bước đã dịch để giải mã
        return jsonify({'decrypted_message': caesar_cipher.decrypt_text(text, key)})
    except KeyError as e:
        return jsonify({"error": f"Missing required key: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
# Vigenere CIPHER ALGORITHM
vigenere_cipher = VigenereCipher()  # Tạo đối tượng mã hóa Vigenere

@app.route('/api/vigenere/encrypt', methods=['POST']) 
def vigenere_encrypt():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON data"}), 400
        plain_text = data['plain_text']  # Văn bản cần mã hóa
        key = data['key']                # Khóa mã hóa
        encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
        return jsonify({'encrypted_text': encrypted_text})
    except KeyError as e:
        return jsonify({"error": f"Missing required key: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON data"}), 400
        cipher_text = data['cipher_text']  # Văn bản đã mã hóa
        key = data['key']                  # Khóa giải mã
        decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
        return jsonify({'decrypted_text': decrypted_text})
    except KeyError as e:
        return jsonify({"error": f"Missing required key: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# RailFence Cipher
railfence_cipher = RailFenceCipher()

@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON data"}), 400
        plain_text = data['plain_text']
        key = int(data['key'])
        encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
        return jsonify({'encrypted_text': encrypted_text})
    except KeyError as e:
        return jsonify({"error": f"Missing required key: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON data"}), 400
        cipher_text = data['cipher_text']
        key = int(data['key'])
        decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
        return jsonify({'decrypted_text': decrypted_text})
    except KeyError as e:
        return jsonify({"error": f"Missing required key: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# PlayFair Cipher
playfair_cipher = PlayFairCipher()

@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON data"}), 400
        key = data['key']
        playfair_matrix = playfair_cipher.create_playfair_matrix(key)
        return jsonify({"playfair_matrix": playfair_matrix})
    except KeyError as e:
        return jsonify({"error": f"Missing required key: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON data"}), 400
        plain_text = data['plain_text']
        key = data['key']
        playfair_matrix = playfair_cipher.create_playfair_matrix(key)
        encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
        return jsonify({'encrypted_text': encrypted_text})
    except KeyError as e:
        return jsonify({"error": f"Missing required key: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON data"}), 400
        cipher_text = data['cipher_text']
        key = data['key']
        playfair_matrix = playfair_cipher.create_playfair_matrix(key)
        decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
        return jsonify({'decrypted_text': decrypted_text})
    except KeyError as e:
        return jsonify({"error": f"Missing required key: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Transposition Cipher
transposition_cipher = TranspositionCipher()

@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON data"}), 400
        plain_text = data.get('plain_text')
        key = int(data.get('key'))
        encrypted_text = transposition_cipher.encrypt(plain_text, key)
        return jsonify({'encrypted_text': encrypted_text})
    except KeyError as e:
        return jsonify({"error": f"Missing required key: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON data"}), 400
        cipher_text = data.get('cipher_text')
        key = int(data.get('key'))
        decrypted_text = transposition_cipher.decrypt(cipher_text, key)
        return jsonify({'decrypted_text': decrypted_text})
    except KeyError as e:
        return jsonify({"error": f"Missing required key: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # Chạy server ở cổng 5000
