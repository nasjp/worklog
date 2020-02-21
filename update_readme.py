#!/usr/bin/env python

import os
from typing import List

log_dir = "logs"


class Log:
    end_token = "[END]"

    def __init__(self, raw_title: str, path: str):
        self.path = path
        self.is_end = self.end_token in raw_title
        self.title = raw_title.rstrip(self.end_token)

    def markdown_link(self) -> str:
        link = "- [{0}] [{1}]({2})".format(self.status(), self.title, self.path)
        return link

    def status(self) -> str:
        if self.is_end:
            return "x"
        return " "


class ReadMe:
    def __init__(self):
        self.logs: List[Log] = []

    def add_log(self, log: Log):
        self.logs.append(log)

    def write(self):
        with open("README.md", mode="w") as f:
            f.write("# work log\n\n")

            for log in self.logs:
                f.write(log.markdown_link() + "\n")


def main():
    log_file_names = os.listdir(log_dir)

    readme = ReadMe()

    for log_file_name in log_file_names:
        path = log_dir + "/" + log_file_name
        with open(path) as f:
            title = f.readline()[2:-1]
            log = Log(title, path)
            readme.add_log(log)

    readme.write()


if __name__ == "__main__":
    main()
