# continous_control_PPO
*Continous control project for the udacity deep reinforcement learning nanodegree*

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

```cd navigation4banana```

Then proceed to installing the required packages by running

```pip install -r requirements.txt```

Having installed all the required packages, the unity environment files can then be downloaded and placed in the banana_env folder. Below are links to download the unity environments for the popular operating systems;

[linux](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Linux.zip) <br/>
[mac](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher.app.zip) <br/>
[windows 32-bit](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86.zip) <br/>
[windows 64-bit](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86_64.zip) <br/>

Also, the PLATFORM variable in the config.py file has to be modified accordingly.

Now, all is set for the experiments

