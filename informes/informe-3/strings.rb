# Recursive functions that returns if a string is palindrome
# Time Complexity: O(|s|)
def IsPalindrome(s, l, r)
  if l > r
    return true
  end
  if s[l] == s[r]
    return IsPalindrome(s, l + 1, r - 1)
  else
    return false
  end
end

# Lowercase characters are changed into uppercase and the original string
# is modified because they are passed by reference
def ToUpper(s)
  n = s.length()
  for i in 0 ... n do
    if 97 <= s[i].ord && s[i].ord <= 122
      s[i] = (s[i].ord - 32).chr
    end
  end
end

# Direct string declaration
name1 = "Manuel"
name2 = "Alejandro"
name3 = "Ana"

raise "Error in IsPalindrome" unless !IsPalindrome(name1, 0, name1.length() - 1)
raise "Error in IsPalindrome" unless !IsPalindrome(name2, 0, name2.length() - 1)
raise "Error in IsPalindrome" unless !IsPalindrome(name3, 0, name3.length() - 1)
# Strings can be assigned as common variables
name4 = name3
# Eventhough "Ana" is not a palindrome
raise "Error in IsPalindrome" unless !IsPalindrome(name4, 0, name4.length() - 1)
ToUpper(name4)
# Now "ANA" is a palindrome
raise "Error in IsPalindrome" unless IsPalindrome(name4, 0, name4.length() - 1)
puts "All tests are OK"
