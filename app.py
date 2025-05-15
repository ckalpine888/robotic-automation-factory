from AutomationFactory import AutomationFactory

if __name__ == "__main__":
    automation_factory = AutomationFactory()
    print(automation_factory.sort(width=10, height=10, length=10, mass=20))
    print(automation_factory.sort(width=-10, height=10, length=10, mass=20))
    print(automation_factory.sort(width=100000, height=10, length=10, mass=20))
    print(automation_factory.sort(width=1, height=10, length=10, mass=2))
