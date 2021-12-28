# O(nlogn)
class Solution:
  def can_make_progression(self, arr: list[int]) -> bool:
    """ Return true if list can be rearranged into arithmetic progression """
    arr = sorted(arr)
    increment = arr[1] - arr[0]

    for i in range(len(arr) - 1):
      cur, next = arr[i], arr[i+1]

      if next - cur != increment:
        return False
    
    return True


if __name__ == '__main__':
  case1 = [1,2]
  case2 = [1,3,4,5,6]
  case3 = [1,2,4]
  case4 = [4,2,1]
  case5 = [1,3,5,7]

  print(Solution().can_make_progression(case1))
  print(Solution().can_make_progression(case2))
  print(Solution().can_make_progression(case3))
  print(Solution().can_make_progression(case4))
  print(Solution().can_make_progression(case5))
