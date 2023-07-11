class Solution(object):
    def romanToInt(self, s):
      Symbol_Values={
          'I':1,
          'V':5,
          'X':10,
          'L':50,
          'C':100,
          'D':500,
          'M':1000,
      }
      result=0


      for i in range (len(s)):
          if i< len(s)-1 and Symbol_Values[s[i]] < Symbol_Values[s[i+1]]:
            result -=Symbol_Values[s[i]]
          else:
              result +=Symbol_Values[s[i]]
      return result