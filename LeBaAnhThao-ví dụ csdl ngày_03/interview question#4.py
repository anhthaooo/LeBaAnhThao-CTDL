def are_anagrams(word1, word2):
    # Sắp xếp các ký tự trong word1 và word2
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)
    
    # So sánh các từ đã sắp xếp
    return sorted_word1 == sorted_word2

# Kiểm tra hàm
print(are_anagrams('listen', 'silent'))   
print(are_anagrams('triangle', 'integral')) 
print(are_anagrams('hello', 'world'))       
