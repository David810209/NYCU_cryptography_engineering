import hashlib
import time

def find_matching_word(file_path, target_hash):
    attempt_count = 0  
    start_time = time.time()  
    
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()  
            for word in words:
                attempt_count += 1  
                encoded_word = hashlib.sha1(word.encode()).hexdigest()
                if encoded_word == target_hash:
                    return word, attempt_count, time.time() - start_time  
    return None, attempt_count, time.time() - start_time 

def find_matching_word_c(file_path, target_hash):
    attempt_count = 0  
    start_time = time.time()  
    s = find_matching_word(salt)
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()  
            for word in words:
                word =  s + word
                attempt_count += 1  
                encoded_word = hashlib.sha1(word.encode()).hexdigest()
                if encoded_word == target_hash:
                    return word, attempt_count, time.time() - start_time  
    return None, attempt_count, time.time() - start_time 

file_path = 'password.txt'
salt = 'dfc3e4f0b9b5fb047e9be9fb89016f290d2abb06'
target_hash = '9d6b628c1f81b4795c0266c0f12123c1e09a7ad3'

matching_word, attempts, duration = find_matching_word_c(file_path, target_hash)
#if want to do 1_c run find_matching_word_c
print(f"Hash: {target_hash}")
print(f"Password: {matching_word}")
print(f"Took {attempts} attempts to crack input hash. Time Taken: {duration:.10f} seconds")
