def process_string(s):
    vowels = "aoyeuiAOYEUI"
    result = ""
    
    for char in s:
        if char not in vowels:
            result += "." + char.lower()
    
    return result

s = input().strip()
print(process_string(s))
