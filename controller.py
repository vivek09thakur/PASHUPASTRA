import threading
from astra.bots.worker import Worker


class BotController:
    def __init__(self, credentials):
        self.credentials = credentials
        self.threads = []

    def run_bot(self, username, password, session_file):
        worker = Worker(username, password, session_file)
        worker.like_and_save_by_hashtag("hinduism", limit=10, min_delay=5, max_delay=10)

    def start_all_bots(self):
        for username, password, session_file in self.credentials:
            thread = threading.Thread(target=self.run_bot, args=(username, password, session_file))
            self.threads.append(thread)
            thread.start()

    def wait_for_completion(self):
        for thread in self.threads:
            thread.join()
        print("All bots have finished.")


if __name__ == "__main__":
    credentials = [
        ("marshal_jon333", "dollar@1357", "session1.json"),
        ("bot2_username", "bot2_password", "session2.json"),
        ("bot3_username", "bot3_password", "session3.json"),
    ]

    controller = BotController(credentials)
    controller.start_all_bots()
    controller.wait_for_completion()