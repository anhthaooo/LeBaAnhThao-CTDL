def is_palindrome(s):
    # Loại bỏ các khoảng trắng và chuyển thành chữ thường
    s = s.replace(" ", "").lower()
    
    # Đặt con trỏ ở đầu và cuối chuỗi
    left = 0
    right = len(s) - 1
    
    while left < right:
        # So sánh ký tự tại vị trí left và right
        if s[left] != s[right]:
            return False
        # Di chuyển con trỏ
        left += 1
        right -= 1
    
    return True

# Kiểm tra chuỗi đối xứng
print(is_palindrome("abcba"))  # True
print(is_palindrome("anhna"))  # True
print(is_palindrome("anhthao"))  # False
