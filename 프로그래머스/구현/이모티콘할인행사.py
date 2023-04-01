def solution(users, emoticons):
    data = [10 ,20, 30, 40]
    discount = []

    # 이모티콘 할인율 구하기
    def dfs(temp, depth):
        if depth == len(temp):
            discount.append(temp[:])
            return
        for d in data:
            temp[depth] += d
            dfs(temp, depth + 1)
            temp[depth] -= d
    dfs([0] * len(emoticons), 0)
    ans = []
    for dis in discount:
        # [10, 10]
        tmp = [0,0]
        for user in users:
            userBuy = 0
            for i in range(len(emoticons)):
                if dis[i] >= user[0]:
                    userBuy += emoticons[i] - emoticons[i] * dis[i] / 100
            if userBuy >= user[1]:
                tmp[0] += 1
            else:
                tmp[1] += userBuy
        ans.append(tmp)
    ans.sort(key=lambda x:(x[0], x[1]))
    return ans[-1]

