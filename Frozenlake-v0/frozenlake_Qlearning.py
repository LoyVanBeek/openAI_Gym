#! /usr/bin/env python

import datetime

import gym
from gym import wrappers
env = gym.make('FrozenLake-v0')
env = wrappers.Monitor(env, "/tmp/Frozenlake-{}".format(str(datetime.datetime.now())))

print "Actions: ", env.action_space
print "Observations: ", env.observation_space

import numpy as np

Q = np.zeros([env.observation_space.n, env.action_space.n])
lr = 0.81
y = 0.96

num_episodes = 10000
reward_list = []

for episode in range(num_episodes):
    reward_all = 0

    observation = env.reset()
    for t in range(100):
        #env.render()
        
        #print observation

        # Reduce noise with each episode and rely more on learning
        noise = np.random.randn(1, env.action_space.n)*(1./(episode+1))
        action = np.argmax(Q[observation,:] + noise)
        next_observation, reward, done, info = env.step(action) 

        Q[observation, action] += lr*(reward + y*np.max(Q[next_observation,:]) - Q[observation, action])

        reward_all += reward
        observation = next_observation
        if done:
            #print("Episode finished after {} timesteps. Reward: {}".format(t+1, reward_all))
            break

    reward_list += [reward_all]

print "Score over time: " +  str(sum(reward_list)/num_episodes)

print Q