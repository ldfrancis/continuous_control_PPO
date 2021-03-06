# continuous_control_PPO
*continuous control project for the udacity deep reinforcement learning nanodegree*

This is the second project for the udacity deep reinforcement learning nanaodegree program. In this project the aim is to train an agent in an environment to perform a task of moving an arm to a target location and keeping it in this location throughout.

The environment provides the agent with a reward of +0.1 for each step that the arm is in the target location.

The observation space of the environment is continuous, having a 33 dimensional vector. The action space is also continuous. It has a 4 dimensional vector with each element value in [-1,1]. The content of the observation corresponds to the position, rotation, velocity, and angular velocity of the arm while that of the action corresponds to the torque applied to the two joints of the arm.

## Getting Started
This project uses python 3 and some of its packages. To get started, first, install anaconda/miniconda  and then create the conda environment using;

```conda create --name=drlndcontcntrl python=3.6```

```source activate drlndcontcntrl```

Clone the repository

```git clone https://github.com/ldfrancis/continuous_control_PPO.git```

Change the current working directory to the projects base folder

```cd continuous_control_PPO```

Then proceed to installing the required packages by running

```pip install -r requirements.txt```

Having installed all the required packages, the unity environment files can then be downloaded and placed in the reacher_env folder. Below are links to download the unity environments for the popular operating systems;

[linux](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Linux.zip) <br/>
[mac](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher.app.zip) <br/>
[windows 32-bit](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86.zip) <br/>
[windows 64-bit](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86_64.zip) <br/>

Also, the PLATFORM variable in the config.py file has to be modified accordingly.

Now, all is set for the experiments

## Instructions
To run the experiment use the commands below:

Train an agent in the environment;

```python main.py train```

Evaluate a trained agent

```python main.py test```

This would use the default configs specified in ```config.py```. The file config.py contains variables whose values are necessary to configure the environment, the agent, and the experiment. Below is a sample setting for the variables in config.py
```
...
ENV_PATH = f"./reacher_env/{ENV_FILE}"
NUM_OBS = 33
NUM_ACT = 4
TARGET_SCORE = 30

# ppo agent
BATCH_SIZE = 64
GAMMA = 0.9
LAMBDA = 0.8
POLICY_HIDDEN_DIM = [64, 32]
CRITIC_HIDDEN_DIM = [64, 32]
MAX_LOG_STD = 0
MIN_LOG_STD = -20
ENTROPY_WEIGHT = 0.005
EPOCHS = 10
POLICY_LR = 5e-5
CRITIC_LR = 5e-5
CLIP_EPSILON = 0.2
```

The experiment would continue running for several episodes till the agent achieves a score of 30 averaged over the last 100 episodes.

## Report
A report containing the results can be found [here](report.md)
