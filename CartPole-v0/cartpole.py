#! /usr/bin/env python

import gym
env = gym.make('CartPole-v0')
env.reset()
for _ in range(1000):
    env.render()
    
    step = env.action_space.sample() # take a random action
    obs, reward, done, info = env.step(step) 

    if done:
        env.reset()
