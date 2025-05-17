def strictEqual(a, b):
  return a == b and type(a) == type(b)

def deepEqual(a, b):
  if type(a) != type(b):
    return False
  if type(a) == type({}):
    if len(a.keys()) != len(b.keys()):
      return False
    for item in a.keys():
      if item.startswith("__") and item.endswith("__") or item in ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']:
        continue
      if b.get(item) is None and a[item] is not None:
        return False 
      if type(a[item]) != type(b[item]):
        return False
      if type(a[item]) == type({}) or type(a[item]) == type([]):
        if not deepEqual(a[item], b[item]):
          return False
      else:
        if not strictEqual(a[item], b[item]):
          return False
    return True
  if type(a) == type([]):
    if len(a) != len(b):
      return False
    for i in range(len(a)):
      if type(a[i]) != type(b[i]):
        return False
      if type(a[i]) == type({}) or type(a[i]) == type([]):
        if not deepEqual(a[i], b[i]):
          return False
      else:
        if not strictEqual(a[i], b[i]):
          return False
    return True 
    
def test(title, needed, target, summary = ""):
  print(f"Execute: {title}; Summary: {'Nothing' if summary == '' else summary}")
  if type(needed) == type({}) or type(needed) == type([]):
    print(f"Result: {'Pass' if deepEqual(needed, target) else 'Fail'}")
  else:
    print(f"Result: {'Pass' if strictEqual(needed, target) else 'Fail'}")