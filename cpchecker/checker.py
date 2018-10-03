import os

import yaml


class Checker(object):

    def __init__(self, config_path):
        self.config_path = config_path
        self.config_contents = self.open_config(config_path)

    @staticmethod
    def open_config(config_path):
        """docstring"""
        with open(config_path, "r") as f:
            return yaml.load(f)

    def get_save_location(self):
        """docstring"""
        return self.config_contents["commands location"]

    def get_commands_location(self):
        """docsting"""
        commands_dir_path = self.config_contents["location"]
        return os.path.join(commands_dir_path, "cp_commands.txt") 

    def get_failed_task_names(self):
        """docstring"""
        save_location_path = self.get_save_location()
        failed_names = []
        results_dir_path = os.path.join(save_location_path, "raw_data")
        results_dirs = os.listdir(results_dir_path)
        # check within each results dir that it contains at least one csv file
        for directory in results_dirs:
            full_path = os.path.join(results_dir_path, directory)
            n_csvs = len(os.listdir(full_path))
            if n_csvs == 0:
                failed_names.append(directory)
        return failed_names

    def get_commands(self):
        """docstring"""
        commands_path = self.get_commands_location()
        with open(commands_path, "r") as f:
            commands = [i.strip() for i in f.readlines()]
        return commands

    def get_failed_task_ids(self):
        """docstring"""
        # get which line in commands corresponds to the failed task name
        # which will be the task_ID number
        task_ids = []
        commands = self.get_commands()
        failed_task_names = self.get_failed_task_names()
        for task_name in failed_task_names:
            for task_id, command in enumerate(commands, 1):
                if task_name in command:
                    task_ids.append(task_id)
        return task_ids
