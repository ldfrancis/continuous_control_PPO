from collections import namedtuple, deque
import numpy as np
import random
print(__name__)

from config import BUFFER_SIZE, BATCH_SIZE


class ReplayBuffer:

    def __init__(self, num_envs=20):
        self.states, self.actions, self.rewards = [],[],[]
        self.values, self.dones, self.log_probs = [],[],[]
        self.num_envs = num_envs

    def reset(self):
        self.states, self.actions, self.rewards = [], [], []
        self.values, self.dones, self.log_probs = [], [], []

    def add_trajectory(self, states, actions, rewards, next_states, dones):
        for i in range(self.num_envs):
            states[i] = states[i] + [next_states[i][-1]]

    def get(self):


        self.reset()


class TrajectoryPrep:

    def __init__(self, num_envs = 20):
        self.num_envs = num_envs
        self.states = [[] for _ in range(num_envs)]
        self.actions = [[] for _ in range(num_envs)]
        self.rewards = [[] for _ in range(num_envs)]
        self.values = [[] for _ in range(num_envs)]
        self.dones = [[] for _ in range(num_envs)]
        self.log_probs = [[] for _ in range(num_envs)]

    def reset(self):
        self.states = [[] for _ in range(self.num_envs)]
        self.actions = [[] for _ in range(self.num_envs)]
        self.rewards = [[] for _ in range(self.num_envs)]
        self.values = [[] for _ in range(self.num_envs)]
        self.dones = [[] for _ in range(self.num_envs)]
        self.log_probs = [[] for _ in range(self.num_envs)]

    def add(self, states, actions, rewards, values, dones, log_probs):
        for i in range(self.num_envs):
            self.states[i] += [states[i]]
            self.actions[i] += [actions[i]]
            self.rewards[i] += [rewards[i]]
            self.values[i] += [values[i]]
            self.dones[i] += [dones[i]]
            self.log_probs[i] += [log_probs[i]]

    def get(self):
        states = self.states
        actions = self.actions
        rewards = self.rewards
        values = self.values
        dones = self.dones
        log_probs = self.log_probs
        self.reset()
        return states, actions, rewards, values, dones, log_probs


def compute_gae(next_value, rewards, dones, values, gamma, tau):
    values += [next_value]
    gae = 0
    returns = []

    for i in reversed(range(len(rewards))):
        td_error = rewards[i] + gamma * values[i+1] * (1-dones[i]) - values[i]
        gae = td_error + gamma*tau*(1-dones[i])*gae
        returns = [gae] + returns

    return returns