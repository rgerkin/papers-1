import ace

class PtrType(ace.Type):
  def __init__(self, target_type, addr_space):
    self.target_type = target_type
    self.addr_space = addr_space
        
  def resolve_Subscript(self, context, node):
    slice_type = context.resolve(node.slice)
    if isinstance(slice_type, IntegerType):
      return self.target_type
    else:
      raise TypeError('<error message>', node)
       
  def translate_Subscript(self, context, node):
    value = context.translate(node.value)
    slice = context.translate(node.slice)
    return ace.copy_node(node, 
      value=value, slice=slice,    
      code=value.code + '[' + slice.code + ']')      
  
  # ...
  
def gptr(target_type):
    return PtrType(target_type, "__global")