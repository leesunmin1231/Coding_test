def solution(name):
    ans = 0
    minMove = len(name) - 1
    for i, word in enumerate(name):
        if word <= 'N':
            ans += ord(word) - ord('A')
        else:
            ans += ord('Z') - ord(word) + 1
        j = i + 1
        while j < len(name) and name[j] == 'A':
            j += 1
        minMove = min(minMove, i * 2 + len(name) - j, 2 * (len(name) - j) + i)
    return ans + minMove