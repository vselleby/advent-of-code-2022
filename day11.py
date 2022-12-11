class Monkey:
    def __init__(self, starting_items, operation, test):
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.items_handled = 0

    def handle_item(self, use_lcm):
        self.items_handled += 1
        item = self.operation(self.items.pop(0))
        if use_lcm:
            # 9699690 is the lcm of all divisible denominators.
            item = item % 9699690
        else:
            item = item // 3
        monkey_receiver = self.test(item)
        return monkey_receiver, item


def solve_a(monkeys):
    for i in range(20):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                monkey_receiver, item = monkey.handle_item(False)
                monkeys.__getitem__(monkey_receiver).items.append(item)
    monkeys.sort(key=lambda x: x.items_handled)
    return monkeys[-1].items_handled * monkeys[-2].items_handled


def solve_b(monkeys):
    for i in range(10000):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                monkey_receiver, item = monkey.handle_item(True)
                monkeys.__getitem__(monkey_receiver).items.append(item)
        if divisible(i, 100):
            print("Round: " + str(i))
    monkeys.sort(key=lambda x: x.items_handled)
    return monkeys[-1].items_handled * monkeys[-2].items_handled


def divisible(x, y):
    if x == 0:
        return False
    return (x % y) == 0


def load_monkeys():
    return [Monkey([73, 77], lambda x: x * 5, lambda y: 6 if divisible(y, 11) else 5),
            Monkey([57, 88, 80], lambda x: x + 5, lambda y: 6 if divisible(y, 19) else 0),
            Monkey([61, 81, 84, 69, 77, 88], lambda x: x * 19, lambda y: 3 if divisible(y, 5) else 1),
            Monkey([78, 89, 71, 60, 81, 84, 87, 75], lambda x: x + 7, lambda y: 1 if divisible(y, 3) else 0),
            Monkey([60, 76, 90, 63, 86, 87, 89], lambda x: x + 2, lambda y: 2 if divisible(y, 13) else 7),
            Monkey([88], lambda x: x + 1, lambda y: 4 if divisible(y, 17) else 7),
            Monkey([84, 98, 78, 85], lambda x: x * x, lambda y: 5 if divisible(y, 7) else 4),
            Monkey([98, 89, 78, 73, 71], lambda x: x + 4, lambda y: 3 if divisible(y, 2) else 2)]


if __name__ == '__main__':
    monkey_list = load_monkeys()
    print(solve_b(monkey_list))
