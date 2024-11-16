import sys
input = sys.stdin.readline  # sys.stdin.readline이 가장 빠른가


N = int(input()) # 수열 길이 
A = [*map(int, input().split())] # 수열
LIS = [A[0]] 


# binary search
def findPlace(e):
    start = 0
    end = len(LIS) - 1
    
    # e 들어갈 위치 찾기
    while start <= end:
        mid = (start + end) // 2
        
        if LIS[mid] == e:  # 정확히 일치
            return mid
        elif LIS[mid] < e:  # 현재 값보다 작으면 오른쪽 search
            start = mid + 1
        else:  # 현재 값보다 크면 왼쪽 search
            end = mid - 1
            
    return start  

# LIS 갱신
for item in A:
    if LIS[-1] < item:  # LIS 마지막 값보다 크면 추가
        LIS.append(item)
    else:  
        idx = findPlace(item)
        LIS[idx] = item  


print(len(LIS))
