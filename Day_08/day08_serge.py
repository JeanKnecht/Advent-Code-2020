from pprint import pprint

# toevoegen input in lijst
filename = "input_test.txt"
with open(filename, "r") as input:
    instructions = [line.strip("\n").split(" ")
                    for line in input.readlines() if line]
    instructions = [(instruction[0], int(instruction[1]), False)
                    for instruction in instructions]

pprint(instructions)


class Runner:
    def __init__(self, instructions):
        self.instructions = instructions
        self.length = len(self.instructions)
        self.pos = 0  # the position, line index
        self.val = 0  # the value
        self.steps = 0
        self.operations = {
            "nop": self.nop,
            "acc": self.acc,
            "jmp": self.jmp,
        }

    def validate(self):
        op_string, op_value, op_visited = self.instructions[self.pos]

        #while instruction not yet visited
        if op_visited:
            return False

        # set instruction VISITED = TRUE
        self.instructions[self.pos] = (op_string, op_value, True)
        self.steps += 1
        return True

    def step(self, debug=False):
        op_string, op_value, op_visited = self.instructions[self.pos]
        op_function = self.operations[op_string]
        op_function(op_value)
        if debug:
            print(f"{op_string}, {op_value} --> {self}")

    def set_position(self, delta):
        self.pos = (self.pos + delta) % self.length

    def nop(self, value):
        self.set_position(+1)
    
    def acc(self, value):
        self.val += value
        self.set_position(+1)
    
    def jmp(self, value):
        self.set_position(value)

    
    def __str__(self):
        return f"pos: {self.pos}, val: {self.val}, \t line: {self.instructions[self.pos]}"


runner = Runner(instructions=instructions)
print("BEFORE RUN:", runner)
print("-" * 20)
while runner.validate():
    runner.step(debug=False)
print("-" * 20)
print("AFTER RUN:", runner)
group_result = runner.val

# testing algorithm
if filename == "input_test.txt":
    assert group_result == 5, "algorithm failed in " + filename
elif filename == "input_jean.txt":
    assert group_result == 1939, "algorithm failed in " + filename
elif filename == "input_serge.txt":  # test added if we want to make changes at a later date
    assert group_result == 1137, "algorithm failed in " + filename
