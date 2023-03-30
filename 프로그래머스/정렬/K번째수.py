def solution(array, commands):
    ans = []
    for cmd in commands:
        ans.append(sorted(array[cmd[0]-1: cmd[1]])[cmd[2]-1])
    return ans