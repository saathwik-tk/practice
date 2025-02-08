## print all subsequence of an array

arr=[3,1,2]
n=len(arr)
def print_all_subseq(ind,arr,print_arr,n):
    if ind== n:
        print(print_arr)
        return 
    print_all_subseq(ind+1,arr,print_arr,n)
    print_arr.append(arr[ind])

    print_all_subseq(ind+1,arr,print_arr,n)
    print_arr.pop(-1)

print_all_subseq(0,arr,[],n)
