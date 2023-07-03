function solution(play_list, listen_time) {
  const numSongs = play_list.length;
  let totalPlayTime = play_list.reduce((acc, cur) => acc + cur, 0);
  let maxNumSongs = 0;

  // 음악을 모두 들을 수 있는 경우
  if (totalPlayTime <= listen_time) {
    return numSongs;
  }

  let windowSum = 0;
  let windowStart = 0;

  for (let windowEnd = 0; windowEnd < numSongs; windowEnd++) {
    windowSum += play_list[windowEnd];

    // 윈도우 크기를 조절하여 listen_time을 초과하는 경우
    while (windowSum > listen_time) {
      windowSum -= play_list[windowStart];
      windowStart++;
    }

    // 현재 윈도우 크기에 해당하는 곡 개수를 최댓값으로 업데이트
    maxNumSongs = Math.max(maxNumSongs, windowEnd - windowStart + 1);
  }

  return maxNumSongs;
}

// 입출력 예시 테스트
console.log(solution([2, 3, 1, 4], 3)); // 출력: 3
console.log(solution([1, 2, 3, 4], 5)); // 출력: 4
