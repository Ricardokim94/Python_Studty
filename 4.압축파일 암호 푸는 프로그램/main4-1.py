import itertools

pw_string ="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for len in range(1,5):
    to_attempt = itertools.product(pw_string, repeat= len) #모든 문자열을 repeat=길이 로 정렬하여 반환합니다.
    for attempt in to_attempt:      #정렬하여 반환된 문자의 수만큼 반복합니다.
        pw = ''.join(attempt)       #리스트로 반환된 값을 문자열로 반환합니다. ''.join(리스트)는 리스트의 값을 문자열로 변환합니다.
        print(pw)