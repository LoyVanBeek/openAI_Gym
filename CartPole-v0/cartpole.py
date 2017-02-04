#! /usr/bin/env python

import datetime

import gym
from gym import wrappers
env = gym.make('CartPole-v0')
env = wrappers.Monitor(env, "/tmp/cartpole-{}".format(str(datetime.datetime.now())))

print "Actions: ", env.action_space
print "Observations: ", env.observation_space

for episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        
        print observation

        action = env.action_space.sample() # take a random action
        observation, reward, done, info = env.step(action) 

        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
