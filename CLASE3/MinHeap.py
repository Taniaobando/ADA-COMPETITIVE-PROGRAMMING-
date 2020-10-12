
class minheap(object):
  """implements a minimal heap without a size restriction"""

  def __init__(self):
    """create a variable-size empty minheap"""
    self.__h = list()

  def __str__(self):
    """return a string representation of the minheap"""
    return str(self.__h)

  def __len__(self):
    """return the size of the minheap"""
    return len(self.__h)

  def is_empty(self):
    """return if the collection is empty or not"""
    return len(self)==0

  def __left(self,i):
    """return the index of the left children of i"""
    return 1+(i<<1)
  
  def __right(self,i):
    """return the index of the right children of i"""
    return (1+i)<<1

  def __parent(self,i):
    """return the index of the parent of i"""
    assert i>0
    return (i-1)>>1

  def get_min(self):
    """return the minimum element of the heap"""
    assert len(self)!=0
    return self.__h[0]

  def __heapify_up(self,i):
    """moves the element up in the tree assuming that the rest of the tree
       satisfies the heap property
    """
    assert i>=0
    if i!=0:
      ip = self.__parent(i)
      if self.__h[ip]>self.__h[i]:
        self.__h[ip],self.__h[i] = self.__h[i],self.__h[ip]
        self.__heapify_up(ip)

  def __heapify_down(self,i):
    """moves the element down in the tree assuming that the rest of the
       tree satisfies the heap property
    """
    il,ir,ib = self.__left(i),self.__right(i),i
    if il<len(self) and self.__h[i]>self.__h[il]: ib = il
    if ir<len(self) and self.__h[ib]>self.__h[ir]: ib = ir
    if ib!=i:
      self.__h[i],self.__h[ib] = self.__h[ib],self.__h[i]
      self.__heapify_down(ib)
    
  def insert(self,x):
    """insert x in the minheap"""
    self.__h.append(x)
    if len(self)>1:
      self.__heapify_up(len(self)-1)

  def remove_min(self):
    """remove the minimum from the heap"""
    assert len(self)!=0
    self.__h[0] = self.__h[-1]
    self.__h.pop()
    if len(self)>1:
      self.__heapify_down(0)