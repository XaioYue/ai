import gymnasium as gym

# 固定策略的函數
def fixed_strategy(observation):
    position, velocity, angle, angle_velocity = observation

    # 如果車在邊界，優先將其拉回中心
    if position > 2.25:
        return 0
    elif position < -2.25:
        return 1
    
    # 根據杆的角度和角速度決定動作
    if angle < 0:  # 杆向左傾斜
        if angle_velocity < 0:  # 杆向左移動
            return 0  # 向左施加力
        else:  # 杆向右移動
            return 1  # 向右施加力
    else:  # 杆向右傾斜
        if angle_velocity > 0:  # 杆向右移動
            return 1  # 向右施加力
        else:  # 杆向左移動
            return 0  # 向左施加力

env = gym.make("CartPole-v1", render_mode="human")  # 若改用這個，會畫圖
observation, info = env.reset(seed=42)
score = 0
total_time_steps = 0
max_time_steps = 0
num_episodes = 10

for episode in range(num_episodes):  # 運行 10 次
    observation, info = env.reset()
    time_steps = 0
    while True:
        env.render()
        action = fixed_strategy(observation)  # 使用固定策略決定行動
        observation, reward, terminated, truncated, info = env.step(action)
        position, velocity, angle, angle_velocity = observation
        score += reward
        time_steps += 1
        if terminated or truncated:
            if time_steps > max_time_steps:
                max_time_steps = time_steps
            total_time_steps += time_steps
            print(f'Episode {episode+1} finished after {time_steps} timesteps, score={score}')
            score = 0
            break

env.close()

print(f'Average timesteps per episode: {total_time_steps / num_episodes}')
print(f'Maximum timesteps in a single episode: {max_time_steps}')
