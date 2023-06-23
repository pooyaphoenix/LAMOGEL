import git
import os
from time import strftime
class HuggingFace():
    def __init__(self) -> None:
        self.MODEL_GIT_PATH: str = "data/models"

    
    def set_up_to_date_with_remote(self) -> any:
        repo = git.Repo(self.MODEL_GIT_PATH)  
        origin = repo.remote("origin")  
        assert origin.exists()
        origin.fetch()
        print("Fetched last changes in remote.")
        return (repo, origin)

    def push_to_hugging_face(self, repo, origin) -> any:

        # model_name: str = ""
        # dir = os.listdir(self.MODEL_GIT_PATH)
        # for i, s in enumerate(dir):
        #     if "azki" in s:
        #         model_name = dir[i]
        #         break

        repo.index.add([]) 
        commit_name: str = ("commited at " + strftime("%Y%m%d-%H%M%S"))
        repo.index.commit(commit_name)
        repo.git.push("--set-upstream", origin, repo.head.ref)
        print("Pushed to hugging-face successfully. ")
  