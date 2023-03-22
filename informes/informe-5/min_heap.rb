class Path
  def initialize weight, node
    @weight = weight
    @node = node
  end
  attr_reader :weight, :node
end

class MinHeap
  MAX = 100
  
  def initialize 
    @heap = Array.new(MAX + 1)
    @len = 0
  end
  attr_reader :len, :heap

  def IsEmpty?
    return @len == 0
  end

  def Push path
    raise  "Insufficient space" unless @len < MAX
    @len += 1
    @heap[@len] = path
    Up()
  end

  def Up
    i = @len
    while i != 1 && IsLess(@heap[i], @heap[i / 2]) do
      @heap[i], @heap[i / 2] = @heap[i / 2], @heap[i]
      i = i / 2
    end
  end

  def IsLess path1, path2
    return path1.weight < path2.weight
  end

  def GetMin
    raise "Empty heap" unless @len > 0
    return @heap[1]
  end
  
  def Pop
    raise "Empty heap" unless @len > 0
    @heap[1] = @heap[@len]
    @len -= 1
    Down(1)
  end

  def Down j
    i = j
    while 2 * i <= @len do
      if 2 * i + 1 <= @len && IsLess(@heap[2 * i + 1], @heap[2 * i]) then
        m = 2 * i + 1
      else
        m = 2 * i
      end     
      
      if IsLess(@heap[m], @heap[i]) then
        @heap[m], @heap[i] = @heap[i], @heap[m]
        i = m
      else
        break
      end      
    end
  end
end
