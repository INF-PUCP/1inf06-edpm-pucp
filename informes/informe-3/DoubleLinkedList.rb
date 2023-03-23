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

  # Push an elemento after the tail
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

  # Push an element before the head
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

  # Removes the tail node
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

  # Removes the head node
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

  # Removes a node with value target in the list. If our target is in our head,
  # then we are going to remove it first being aware of not having a unitary list.
  # Otherwise, we are going to look for the node that is inmediately before of our
  # target and then, we are going to link this one and the one that is inmediately
  # after our target.
  def Remove target
    raise "Empty list" unless self.length > 0
    if target == self.head.value
      if self.head.next == nil
        self.head = self.tail = nil
      else
        self.head.next.prev = nil
        self.head = self.head.next
      end
      self.length -= 1
    else
      current = self.head
      while current != nil && current.next.value != target
        current = current.next
      end
      if current != nil
        if current.next.next != nil
          current.next.next.prev = current
        end
        current.next = current.next.next
        self.length -= 1
      end
    end
  end

  # Prints the list from head to tail. The variable cnt counts the number of
  # nodes we have analized to print the characters that represent the links correctly.
  def Print
    if self.head == nil
      puts "Empty list"
    else
      current = self.head
      cnt = 0
      while current != nil
        if cnt > 0
          print " <-> "
        end
        print current.value
        current = current.next
        cnt += 1
      end
      puts ""
    end
  end
end
