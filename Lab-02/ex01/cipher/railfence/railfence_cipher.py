# Lớp thực hiện mã hóa và giải mã Rail Fence
class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        # Khởi tạo mảng 2D để lưu các ký tự theo số rail (hàng) đã cho
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        # direction: 1 là đi xuống, -1 là đi lên trong ma trận zigzag
        direction = 1

        # Di chuyển theo đường zigzag để điền ký tự vào rails
        for char in plain_text:
            # Thêm ký tự vào rail hiện tại
            rails[rail_index].append(char)
            
            # Xử lý đổi hướng khi chạm rail đầu hoặc cuối
            if rail_index == 0:  # Nếu ở rail đầu, đi xuống
                direction = 1
            elif rail_index == num_rails - 1:  # Nếu ở rail cuối, đi lên
                direction = -1    
            rail_index += direction

        # Ghép tất cả ký tự từ các rail thành chuỗi mã hóa
        cipher_text = "".join("".join(rail) for rail in rails)
        return cipher_text

    def rail_fence_decrypt(self, cipher_text, num_rails):
        # Tính số ký tự trên mỗi rail
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1

        # Tính kích thước của từng rail dựa trên pattern zigzag
        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        # Phân chia cipher text vào các rail theo độ dài đã tính
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(cipher_text[start:start + length])
            start += length

        # Đọc lại các ký tự theo đường zigzag để khôi phục plain text
        plain_text = ""
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            plain_text += rails[rail_index][0]
            rails[rail_index] = rails[rail_index][1:]
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        return plain_text