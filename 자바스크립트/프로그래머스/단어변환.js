function checkNext(node, next){
    const len = node.length
    let count = 0;
    for (let i = 0; i < len; i++){
        if (node[i] === next[i]) count++;
    }
    if (count + 1 === len) return true;
    return false;
}
function solution(begin, target, words) {
    const q = []
    const dist = Array(words.length).fill(0)
    q.push([begin, 0])
    while (q.length !== 0){
        const [node, index] = q.shift()
        if (node === target) return dist[index]
        for (let i = 0; i < words.length; i++){
            if (!checkNext(node, words[i])) continue
            if (dist[i] !== 0) continue
            q.push([words[i], i])
            dist[i] = dist[index] + 1
        }
    }
    return 0
}

console.log('hit','cog',["hot", "dot", "dog", "lot", "log"])