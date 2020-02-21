import datetime
import os
from typing import List

import git

log_dir = "logs"
readme_file = "README.md"


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
        with open(readme_file, mode="w") as f:
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

    repo = git.Repo()
    repo.index.add([log_dir, readme_file])
    repo.index.commit(
        ":memo: Update " + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    )
    repo.remote.push("master")


if __name__ == "__main__":
    main()
