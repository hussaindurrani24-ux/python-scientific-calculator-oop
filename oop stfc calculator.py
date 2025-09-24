import math

HISTORY = "history.txt"
# ---------- Base Class ----------
class Operation:
    """Base class for all operations"""
    def record(self, text):
        with open(HISTORY, "a") as f:
            f.write(text + "\n")

    def execute(self, *args):
        """Each subclass will override this"""
        raise NotImplementedError("Subclass must implement execute()")
# ---------- Subclasses ----------
class BasicOperation(Operation):
    def execute(self, op, a, b):
        result = {"+": a + b, "-": a - b, "*": a * b, "/": a / b}[op]
        self.record(f"Basic {a} {op} {b} = {result}")
        return result

class AdvancedOperation(Operation):
    def execute(self, sub, a, b=None):
        if sub == "power":
            result = a ** b
            self.record(f"{a}^{b} = {result}")
        else:
            result = math.sqrt(a)
            self.record(f"sqrt({a}) = {result}")
        return result

class TrigOperation(Operation):
    def execute(self, sub, x):
        funcs = {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan
        }
        result = funcs[sub](math.radians(x))
        self.record(f"{sub}({x}) = {result}")
        return result

class LogOperation(Operation):
    def execute(self, sub, x):
        funcs = {
            "ln": math.log,
            "log10": math.log10,
            "exp": math.exp
        }
        result = funcs[sub](x)
        self.record(f"{sub}({x}) = {result}")
        return result
# ---------- History Viewing ----------
def show_history():
    try:
        print(open(HISTORY, "r").read())
    except FileNotFoundError:
        print("No history yet.")
# ---------- Main Loop ----------
basic = BasicOperation()
adv = AdvancedOperation()
trig = TrigOperation()
log = LogOperation()

while True:
    print("\n1) Basic  2) Adv  3) Trig  4) Log/Exp  5) History  0) Exit")
    ch = input("Choice: ")
    if ch == "0":
        print("exit")
        break
    elif ch == "1":
        a = int(input("a: "))
        b = int(input("b: "))
        op = input("+ - * /: ")
        res = basic.execute(op, a, b)
    elif ch == "2":
        sub = input("power/sqrt: ")
        if sub == "power":
            a = int(input("a: "))
            b = int(input("b: "))
            res = adv.execute(sub, a, b)
        else:
            a = int(input("a: "))
            res = adv.execute(sub, a)
    elif ch == "3":
        sub = input("sin/cos/tan: ")
        x = int(input("deg: "))
        res = trig.execute(sub, x)
    elif ch == "4":
        sub = input("ln/log10/exp: ")
        x = int(input("x: "))
        res = log.execute(sub, x)
    elif ch == "5":
        show_history()
        continue
    else:
        continue
    print("=", res)
