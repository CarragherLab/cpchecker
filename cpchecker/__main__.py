import sys

from checker import Checker

def main():
    config_path = sys.argv[1]
    results_checker = Checker(config_path)
    failed_task_ids = results_checker.get_failed_task_ids()
    for i in failed_task_ids:
        print(i)


if __name__ == "__main__":
    main()