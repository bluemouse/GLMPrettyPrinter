import gdb
import re

def is_vec(type_name):
    pattern = re.compile(r'glm::vec<([2-4]),\s*(float|double|int|unsigned int|bool),\s*(.*?)>')
    match = pattern.match(type_name)
    return bool(match)

def vec_info(val):
    n = val.type.template_argument(0)
    T = val.type.template_argument(1)
    indices = ['x', 'y', 'z', 'w']
    elements = [format_value(val[indices[i]]) for i in range(n)]
    return n, elements

def is_mat(type_name):
    pattern = re.compile(r'glm::mat<([2-4]),\s*([2-4]),\s*(float|double|int|unsigned int|bool),\s*(.*?)>')
    match = pattern.match(type_name)
    return bool(match)

def format_value(value):
  if value.type.code == gdb.TYPE_CODE_FLT:
    return format(float(value), '.5f')
  else:
    return str(value)

class VecPrinter:
  def __init__(self, val):
    self.val = val
  def to_string(self):
    n, elements = vec_info(self.val)
    return "({})".format(", ".join(elements))

class MatPrinter:
  def __init__(self, val):
    self.val = val
  def to_string(self):
    n = self.val.type.template_argument(0)
    m = self.val.type.template_argument(1)
    return f"mat{n}x{m}"
  def children(self):
    n = self.val.type.template_argument(0)
    m = self.val.type.template_argument(1)
    cols = self.val['value']
    for i in range(n):
      yield f"[{i}]", cols[i]
  def display_hint(self):
    return 'array'

def glm_types_printer(val):
  if val.address == 0 or val.is_optimized_out:
    return "invalid or optimized out"

  val_type = str(val.type.strip_typedefs())
  print(f"val_type = {val_type}")

  # if not 'glm::' in val_type:
  #   return None

  # if val_type.endswith('*'):
  #   return None # we do not want to dereference pointers
  #   # val = val.dereference() # if we do, call this
  # if val_type.endswith('&'):
  #   val = val.dereference()
  # if val_type.startswith('const'):
  #   val = val.unqualified()

  if is_vec(val_type):
    return VecPrinter(val)
  elif is_mat(val_type):
    return MatPrinter(val)

  return None

gdb.pretty_printers.append(glm_types_printer)
