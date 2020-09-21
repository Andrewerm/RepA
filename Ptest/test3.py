# def cool_range(start, stop, inc):
#     x = start
#     while x < stop:
#         yield x
#         x += inc
#
# for n in cool_range(1, 5, 0.5):
#     print(n)

arr1=[1,2,3,4,5,6]
arr2=[4,5,6,7,8,20]
res=(*arr1, *arr2)
print(res)