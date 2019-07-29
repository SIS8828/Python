class InstanceCounter:
    count = 0

    def __init__(self):
        InstanceCounter.count += 1

    @classmethod
    def print_instance_count(cls):
        print(cls.count)

if __name__ == '__main__':
    a =InstanceCounter()
    InstanceCounter.print_instance_count()

    b = InstanceCounter()
    InstanceCounter.print_instance_count()

    c = InstanceCounter()
    c.print_instance_count()

    InstanceCounter.count = 10

    a.print_instance_count()
    b.print_instance_count()
    c.print_instance_count()
