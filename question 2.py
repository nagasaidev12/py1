class element:
  def twoSum(self, nums, target):
       l= {}
       for i, num in enumerate(nums):
           if target - num in l:
               return (l[target - num], i )
           l[num] = i
print("a=%d, b=%d" % element().twoSum((10,20,10,40,50,60,70),90))
