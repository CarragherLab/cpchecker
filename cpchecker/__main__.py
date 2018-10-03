import sys

from cpchecker.checker import Checker

def main():
    config_path = sys.argv[1]
    results_checker = Checker(config_path)
    for task in results_checker.get_failed_task_ids():
        print(task)


if __name__ == "__main__":
    main()