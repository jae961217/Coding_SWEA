for tc in range(int(input())):
    n=int(input())
    numbers=list(map(int,input().split()))
    cnt=0
    def merge(left, right):
        global cnt
        i, j = 0, 0
        sorted_list = []
        if left[-1]>right[-1]:
            cnt+=1
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1

        while i < len(left):
            sorted_list.append(left[i])
            i += 1
        while j < len(right):
            sorted_list.append(right[j])
            j += 1

        return sorted_list


    def mergeSort(numbers):
        if len(numbers) <= 1:
            return numbers
        mid = len(numbers) // 2
        left = numbers[:mid]
        right = numbers[mid:]

        sorted_left = mergeSort(left)
        sorted_right = mergeSort(right)
        return merge(sorted_left, sorted_right)

    print(f'#{tc+1} {mergeSort(numbers)[len(numbers)//2]} {cnt}')
