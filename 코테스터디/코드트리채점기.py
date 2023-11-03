import heapq

def getDomain(url):
    return url.split("/")[0]

Q = int(input())
arr = []
for _ in range(Q):
    arr.append(input())
taskDic = {} # 각 도메인별 heapq 관리.
waitingJudger = []
running = [] # 채점기 [url, t] or None
runningDic = {} #{도메인: bool}
endTaskDic = {} # 각 도메인별 스택 관리 [url, start, end]
watingDic = {} # {url:bool}
ans = 0
for sen in arr:
    index = int(sen[:3])
    tmp = sen[4:]
    # 채점기 준비
    if index == 100:
        N, u0 = tmp.split(" ")
        # 채점기 초기화
        running = [None for _ in range(int(N)+1)]
        waitingJudger = [i for i in range(1, int(N)+1)]
        # 채점 우선순위가 1인 u0 채점 대기 큐에 들어감.
        taskq = []
        # p: 우선순위, t: 시간, url
        heapq.heappush(taskq, [1,0,u0])
        taskDic[getDomain(u0)] = taskq
        watingDic[u0] = True
        ans += 1
    # 채점 요청
    elif index == 200:
        t, p, u = tmp.split(" ")
        if not getDomain(u) in taskDic:
            taskDic[getDomain(u)] = [[int(p), int(t), u]]
            ans += 1
            watingDic[u] = True
            continue
        if not u in watingDic:
            heapq.heappush(taskDic[getDomain(u)], [int(p), int(t), u])
            watingDic[u] = True
            ans += 1
    # 채점 시도
    elif index == 300:
        t = int(tmp)
        result = []
        # 채점할 후보 뽑아보기
        for domain, taskq in taskDic.items():
            # 채점이 될 수 없는 경우 
            # 현재 채점 진행중인 경우
            if len(waitingJudger) == 0:
                continue
            if domain in runningDic:
                continue
            # 같은 도메인 종료된 시점 고려
            if domain in endTaskDic:
                target = endTaskDic[domain][-1]
                if len(target) != 0 and t < target[1] + 3 * (target[2]-target[1]):
                    continue
            if not taskq:
                continue
            tmp = taskq[0]
            if len(result) == 0:
                result = tmp
                continue
            if tmp[0] < result[0]:
                result = tmp
            elif tmp[0] == result[0] and tmp[1] < result[1]:
                result = tmp
        # 채점할 대상이 없을 경우
        if len(result) == 0:
            continue
        taskp, taskt, url = result
    
        # 쉬고 있는 채점기 찾기
        i = heapq.heappop(waitingJudger)
        # 채점 진행
        running[i] = [url, t]
        runningDic[getDomain(url)] = True
        # taskDic 갱신
        if taskDic[getDomain(url)]:
            heapq.heappop(taskDic[getDomain(url)])
            del watingDic[url]
            if len(taskDic[getDomain(url)]) == 0:
                del taskDic[getDomain(url)]
            ans -= 1
         
    # 채점 종료
    elif index == 400:
        t, J_id = map(int,tmp.split(" "))
        target = running[J_id]
        if not target:
            continue
        running[J_id] = None
        del runningDic[getDomain(target[0])]
        heapq.heappush(waitingJudger, int(J_id))
        if getDomain(target[0]) in endTaskDic:
            endTaskDic[getDomain(target[0])].append([target[0], target[1], t])
        else:
            endTaskDic[getDomain(target[0])] = [[target[0], target[1], t]]
    # 채점 대기 큐 조회
    else:
        t = int(tmp)
        print(ans)