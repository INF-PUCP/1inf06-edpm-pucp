# Returns the maximum value in the array arr
def FindMax(arr)
  n = arr.length()
  maximum = arr[0]
  for i in 1 ... n do
    if arr[i] > maximum
      maximum = arr[i]
    end
  end
  return maximum
end

# Direct declaration as a collection of elements
a1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8]
raise "Error in FindMax" unless FindMax(a1) == 9

# Declaration as an object
a2 = Array.new(5)
for i in 0 ... 5 do
  a2[i] = i
end
raise "Error in constructor" unless a2.length() == 5
raise "Error in FindMax" unless FindMax(a2) == 4

# a : n * m matrix
# b : m * p matrix
# c = a * b :n * p matrix
def MatrixMultiplication(a, b)
  n = a.length()
  m = a[0].length()
  p = b[0].length()
  raise "Input matrices can't be multiplied" unless m == b.length()
  # Creating the empty matrix that is going to store our result
  c = Array.new(n)
  for i in 0 ... n do
    c[i] = Array.new(p)
  end
  for i in 0 ... n do
    for j in 0 ... p do
      c[i][j] = 0
      for k in 0 ... m do
        c[i][j] += a[i][k] * b[k][j]
      end
    end
  end
  return c
end

def PrintMatrix(a)
  n = a.length()
  m = a[0].length()
  for i in 0 ... n do
    for j in 0 ... m do
      print "#{a[i][j]} "
    end
    puts ""
  end
end

# Declaring the matrices that are going to be multiplied
a = [[2, 1, 4], [0, 1, 1]]
b = [[6, 3, -1, 0], [1, 1, 0, 4], [-2, 5, 0, 2]]
c = MatrixMultiplication(a, b)

puts "Matrix a:"
PrintMatrix(a)
puts "Matrix b:"
PrintMatrix(b)
puts "Matrix c = a * b:"
PrintMatrix(c)
