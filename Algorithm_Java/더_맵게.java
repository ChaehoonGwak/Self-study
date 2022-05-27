문제 설명
매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 
  모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

제한 사항
scoville의 길이는 2 이상 1,000,000 이하입니다.
K는 0 이상 1,000,000,000 이하입니다.
scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.
  
  
  
import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> q = new PriorityQueue<>(); // 최솟값 활용해야 하므로 우선순위큐 사용
        
        for(int i = 0; i < scoville.length; i++)
            q.add(scoville[i]);
        
        while(q.size() > 1 && q.peek() < K){ // 우선순위큐에 2개 이상, 최솟값이 K 이상일 때까지
            int minHot = q.poll(); // 가장 맵지 않은 음식
            int secondMinHot = q.poll(); // 두 번째로 맵지 않은 음식
        
            int mixHot = minHot + (secondMinHot * 2); // 섞은 음식의 스코빌 지수
            q.add(mixHot); // 우선순위큐에 삽입
            answer++;
        }
        
        if(q.size() <= 1 && q.peek() < K) // 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
            answer = -1;
            
        return answer;
    }
}
