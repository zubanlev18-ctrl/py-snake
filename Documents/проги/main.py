# def bubble(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
# def insertion(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j+1] = arr[j]
#             j -= 1
#             arr[j+1] = key

# arr = [4324, 5253, 6546, 767, 111, 2, 5454, 776, 100445]
# insertion(arr)
# print(arr)


list = [int(input())]
list.append(0)
end = 4

result = [l for l in list if l % 10 == end]
if result % 3 == 0:
    print(result)