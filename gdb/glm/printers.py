import gdb
import re

def is_vec(type):
    pattern = re.compile(r'glm::vec<([2-4]),\s*(float|double|int|unsigned int|bool),\s*(.*?)>')
    match = pattern.match(str(type))
    return bool(match)

def vec_info(val):
    n = val.type.template_argument(0)
    T = val.type.template_argument(1)
    indices = ['x', 'y', 'z', 'w']
    elements = [format_value(val[indices[i]]) for i in range(n)]
    return n, elements

def is_mat(type):
    pattern = re.compile(r'glm::mat<([2-4]),\s*([2-4]),\s*(float|double|int|unsigned int|bool),\s*(.*?)>')
    match = pattern.match(str(type))
    return bool(match)

def is_quat(type):
    pattern = re.compile(r'glm::qua<(float|double),\s*(.*?)>')
    match = pattern.match(str(type))
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

class QuatPrinter:
  def __init__(self, val):
    self.val = val
  def to_string(self):
    x = format_value(self.val['x'])
    y = format_value(self.val['y'])
    z = format_value(self.val['z'])
    w = format_value(self.val['w'])
    return f"Quaternion [{x}, {y}, {z}, {w}]"


def glm_types_printer(val):
  if val.address == 0 or val.is_optimized_out:
    return "invalid or optimized out"

  if not 'glm::' in str(val.type):
    return None

  if val.type.code == gdb.TYPE_CODE_PTR or val.type.code == gdb.TYPE_CODE_REF:
    val = val.dereference()

  val_type = val.type.unqualified().strip_typedefs()
  val = val.cast(val_type)

  if is_vec(val_type):
    return VecPrinter(val)
  elif is_mat(val_type):
    return MatPrinter(val)
  elif is_quat(val_type):
    return QuatPrinter(val)

  return None

gdb.pretty_printers.append(glm_types_printer)
