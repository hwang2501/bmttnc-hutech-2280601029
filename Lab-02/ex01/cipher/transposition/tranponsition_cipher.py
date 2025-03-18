class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        # text: văn bản cần mã hóa
        # key: số cột dùng để mã hóa (số nguyên dương)
        encrypted_text = ""
        
        # Duyệt qua từng cột
        for col in range(key):
            pointer = col
            # Đọc các ký tự trong cột hiện tại
            # pointer tăng lên key đơn vị để đi tới ký tự tiếp theo trong cùng cột
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        # text: văn bản đã mã hóa
        # key: số cột đã dùng để mã hóa
        # Tạo mảng rỗng có độ dài bằng key để lưu kết quả giải mã
        decrypted_text = [''] * key
        row, col = 0, 0
        
        # Phân phối các ký tự vào đúng vị trí ban đầu
        for symbol in text:
            decrypted_text[col] += symbol
            col += 1
            # Khi đến cuối cột hoặc đã xử lý hết các ký tự dư
            if col == key or (col == key - 1 and row >= len(text) % key):
                col = 0  # Reset về cột đầu tiên
                row += 1  # Chuyển sang hàng tiếp theo
        return ''.join(decrypted_text)
