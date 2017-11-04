"""manages github repos"""
import os
from typing import Optional, Tuple, Any, Dict

import pygit2 as git

from .webhook.handler import Handler


class Manager(object):
    """handles git repos"""

    def __init__(self: Manager, handler: Handler, master: str = "master", test: Optional[str] = None) -> None:
        self.webhook_handler: Handler = handler
        self.repo: git.Repository = self.get_repo()
        self.config: Dict[str, Any] = self.get_config()

    def get_repo(self: Manager) -> git.Repository:
        """clone or initialize repository"""

        repo_folder_name: str = self.webhook_handler.repo_id
        directory = os.path.join(os.getcwd(), repo_folder_name)
        if os.path is not os.path.isdir(directory):
            os.makedirs(directory)
            return git.clone_repository(
                self.webhook_handler.git_url, path=directory)

        # I"m going to assume the repo has already been created
        # dangerous assumption, and it'll bite me in the ass someday
        local_repo: git.Repository = git.Repository(path=directory)
        local_repo.
        return local_repo

    def get_config(self: Manager) -> Dict[str, Any]:
        """gets config file inside repo"""
        import json
        repo_index: git.repository.Index = self.repo.index
        repo_index.read()
        try: 
            config_entry = repo_index["css_updator.json"]
        except KeyError:
            print("no config file exists")
        else: 
            with self.repo[config_entry.id] as blob:
                return json.loads(blob.data)