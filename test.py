# from bisect import bisect_left, bisect_right
# def count_by_range(a, left_value, right_value):
#     print(a)
#     right_index = bisect_right(a, right_value)
#     print(right_index,'right',right_value)
#     left_index = bisect_left(a, left_value)
#     print(left_index,'left',left_value)
#     return right_index - left_index
# words = ['frodo', 'front', 'frost', 'frozen', 'frame', 'kakao']
#
# queries = ['fro??', '????o', 'fr???', 'fro???','pro?']
# for q in queries:
#     print(count_by_range(words,  q.replace('?','a'), q.replace('?','z')))
lst = [1]
print(type(sum(lst)))
