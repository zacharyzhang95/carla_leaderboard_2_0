# This file is used to set parameters of CARLA leadergboard 2.0
# Author: Zachary Zhang
# Version: v0.1
# Edit Date: 14/01/2024

 
# carla setting
export CARLA_ROOT=/home/zc/carla/CARLA_Leaderboard_20
export SCENARIO_RUNNER_ROOT=${CARLA_ROOT}/scenario_runner
export LEADERBOARD_ROOT=${CARLA_ROOT}/leaderboard
export PYTHONPATH="${CARLA_ROOT}/PythonAPI/carla/":"${SCENARIO_RUNNER_ROOT}":"${LEADERBOARD_ROOT}":"${CARLA_ROOT}/PythonAPI/carla/dist/carla-0.9.14-py3.7-linux-x86_64.egg":${PYTHONPATH}

# (XML) — The set of routes that will be used for the simulation. 
export ROUTES=${LEADERBOARD_ROOT}/data/routes_devtest.xml

# (int) — Number of times each route is repeated for statistical purposes.
export REPETITIONS=1

# (int) — Flag that indicates if debug information should be shown during the simulation.
export DEBUG_CHALLENGE=1

# (Python module) — Path to the agent’s Python module.
# export TEAM_AGENT=/home/zc/ST-P3/carla_agent.py
export TEAM_AGENT=/home/zc/ST-P3/carla_agent_6_camera.py
# export TEAM_AGENT=${LEADERBOARD_ROOT}/leaderboard/autoagents/human_agent.py
# export TEAM_AGENT=${LEADERBOARD_ROOT}/leaderboard/autoagents/test_agent.py

# (defined by the user) — Path to an arbitrary configuration file read by the provided agent (model .ckpt file).
export TEAM_CONFIG=/home/zc/ST-P3/models/carla.ckpt
# export TEAM_CONFIG=/home/zc/ST-P3/models/STP3_plan.ckpt

# (JSON) — The name of a file where the Leaderboad metrics will be recorded.
export CHECKPOINT_ENDPOINT=${LEADERBOARD_ROOT}/results.json

# (string) — Track in which the agent is competing. There are two possible options: SENSORS and MAP
export CHALLENGE_TRACK_CODENAME=SENSORS

# Path to save visulise results
export SAVE_PATH=/home/zc/ST-P3/carla_sim_result


# These environment variables are passed to ${LEADERBOARD_ROOT}/leaderboard/leaderboard_evaluator.py, 
# which serves as the entry point to perform the simulation.
# ./scripts/run_evaluation.sh
./carla/CARLA_Leaderboard_20/leaderboard/scripts/run_evaluation.sh
