import gymnasium as gym

# Create the LunarLander environment
env = gym.make("LunarLander-v3", render_mode="human")

env.reset()
for step in range(1000):
    env.render()
    env.step(env.action_space.sample())  # Take a random action

env.close()
