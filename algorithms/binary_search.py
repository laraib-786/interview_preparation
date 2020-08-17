def binary_search(arr,l,h,key):
    if l==h:
        if arr[l]==key:
            return "found"
        else:
            return "not found"

    else:
        mid=(l+h)//2
        if arr[mid]==key:
            return "found"

        elif arr[mid]>key:
            return binary_search(arr,l,mid,key)
        else:
            return binary_search(arr,mid+1,h,key)

print(binary_search([3,6,8,12,14,17,25,29,31,38,42,47,53,55,62],0,14,1000))
