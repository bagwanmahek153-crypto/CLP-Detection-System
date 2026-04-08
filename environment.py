import random
import os


class CLPEnvironment:

    def __init__(self):
        self.images = os.listdir("assets")
        self.state = None

    def reset(self):
        img = random.choice(self.images)

        self.state = {
            "image": f"assets/{img}",
            "speech_score": random.randint(1, 10),
            "age": random.randint(1, 10)
        }
        return self.state

    def step(self, action):
        # correct answer (dummy logic)
        correct = random.randint(0, 2)

        if action == correct:
            reward = 10
        else:
            reward = -5

        done = True

        return self.state, reward, done, {"correct": correct}