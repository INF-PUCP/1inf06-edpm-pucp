class DoubleLinkedList
  
  class Node
    attr_accessor :value, :prev, :next
    
    def initialize value
      self.value = value
      self.prev = nil
      self.next = nil
    end
  end

  attr_accessor :head, :tail, :length

  def initialize
    self.head = nil
    self.tail = nil
    self.length = 0
  end

  def IsEmpty
    return self.length == 0
  end

  def Size
    return self.length
  end

  def Head
    return self.head.value
  end

  def Tail
    return self.tail.value
  end

  def AddRight value
    node = Node.new value
    if self.head == nil
      self.head = node
      self.tail = node
    else
      self.tail.next = node
      node.prev = self.tail
      self.tail = node
    end
      self.length += 1
  end

  def AddLeft value
    node = Node.new value
    if self.head == nil
      self.head = node
      self.tail = node
    else
      self.head.prev = node
      node.next = self.head
      self.head = node
    end
    self.length += 1
  end

  def RemoveRight
    raise "Empty list" unless self.length > 0
    if self.length == 1
      self.head = self.tail = nil
    else
      self.tail = self.tail.prev
      self.tail.next = nil
    end
    self.length -= 1
  end

  def RemoveLeft
    raise "Empty list" unless self.length > 0
    if self.length == 1
      self.head = self.tail = nil
    else
      self.head = self.head.next
      self.head.prev = nil
    end
    self.length -= 1
  end

  def Remove target
    raise "Empty list" unless self.length > 0
    if target == self.head.value
      if self.head.next == nil
        self.head = self.tail = nil
      else
        self.head = self.head.next
      end
      self.length -= 1
    else
      current = self.head
      while current != nil && current.next.value != target
        current = current.next
      end
      if current != nil
        current.next = current.next.next
        self.length -= 1
      end
    end
  end

  def Print
    if self.head == nil
      puts "Empty list"
    else
      current = self.head
      cnt = 0
      while current != nil
        if cnt > 0
          print " -> "
        end
        print current.value
        current = current.next
        cnt += 1
      end
      puts ""
    end
  end
end
