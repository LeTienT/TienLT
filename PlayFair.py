# Hàm để tạo ma trận Playfair từ khóa
def create_playfair_matrix(keyword):
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' 
    matrix = ''
    keyword = keyword.upper().replace('J', 'I')  

    for char in keyword:  
        if char not in matrix:
            matrix += char

    for char in alphabet: 
        if char not in matrix:
            matrix += char

    return matrix

# Hàm để mã hóa văn bản sử dụng ma trận Playfair
def playfair_cipher(plaintext, matrix):
    plaintext = plaintext.upper().replace('J', 'I')  
    ciphertext = ''

    # Chia văn bản thành các cặp ký tự
    pairs = []
    for i in range(0, len(plaintext), 2):
        if i == len(plaintext) - 1:
            pairs.append(plaintext[i] + 'X')  
        elif plaintext[i] == plaintext[i + 1]:
            pairs.append(plaintext[i] + 'X') 
        else:
            pairs.append(plaintext[i:i + 2])

    # Mã hoá từng cặp ký tự
    for pair in pairs:
        char1, char2 = pair
        row1, col1 = divmod(matrix.index(char1), 5)
        row2, col2 = divmod(matrix.index(char2), 5)

        if row1 == row2:
            ciphertext += matrix[row1 * 5 + (col1 + 1) % 5] + matrix[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[((row1 + 1) % 5) * 5 + col1] + matrix[((row2 + 1) % 5) * 5 + col2]
        else:
            ciphertext += matrix[row1 * 5 + col2] + matrix[row2 * 5 + col1]

    return ciphertext

# Hàm để xử lý sự kiện khi nhấn nút
def encrypt_text(keyword, plaintext):
    matrix = create_playfair_matrix(keyword)
    ciphertext = playfair_cipher(plaintext, matrix)

    print("Mã hóa:", ciphertext)

# Nhập keyword và plaintext từ dòng lệnh
keyword = input("Nhập khóa: ")
plaintext = input("Nhập văn bản: ")

encrypt_text(keyword, plaintext)
