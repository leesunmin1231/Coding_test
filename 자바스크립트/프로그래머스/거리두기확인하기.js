function checkPlace(place, start){
    const dr = [0,0,-1,1]
    const dc = [-1,1,0,0]
    for (let i = 0; i < 4; i++){
        const [nr, nc] = [start[0] + dr[i], start[1] + dc[i]]
        if (nr < 0 || nr >= 5) continue;
        if (nc < 0 || nc >= 5) continue;
        if (place[nr][nc] === "P") return false
        if (place[nr][nc] === "X") continue
        for (let j = 0; j < 4; j++){
            if (nr + dr[j] === start[0] && nc + dc[j] === start[1]) continue
            if (nr + dr[j] < 0 || nr + dr[j] >= 5) continue
            if (nc + dc[j] < 0 || nc + dc[j] >= 5) continue
            if (place[nr + dr[j]][nc + dc[j]] === "P") return false
        }
    }
}
function solution(places) {
    const ans = []
    for (const place of places){
        let flag = true
        for (let r = 0; r < 5; r++){
            for (let c = 0; c < 5; c++){
                if (place[r][c] === "P"){
                    const result = checkPlace(place, [r,c])
                    if (result === false) flag = false
                }
            }
        }
        flag ? ans.push(1) : ans.push(0)
    }
    return ans
}