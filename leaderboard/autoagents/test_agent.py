import carla

from leaderboard.autoagents.autonomous_agent import AutonomousAgent
from leaderboard.autoagents.autonomous_agent import Track


def get_entry_point():
    """
    Returns the name of my new class (MyAgent)
    """
    return 'MyAgent'

class MyAgent(AutonomousAgent):

    def setup(self, path_to_conf_file):
        """
        At a minimum, this method sets the Leaderboard modality.

        The self.track attribute should be an enum and not a string. 
        It can only take the possible values Track.SENSORS or Track.MAP
        """
        self.track = Track.SENSORS

    def sensors(self):
        """
        CARLA uses the Unreal Engine coordinate system, which is: x-front, y-right, z-up.
        If a sensor is located more than 3 meters away from its parent in any axis,  the setup will fail.
        """
        sensors = [
            {
                'type': 'sensor.camera.rgb',
                'x': 1.3, 'y': 0.0, 'z': 2.3,
                'roll': 0.0, 'pitch': 0.0, 'yaw': 0.0,
                'width': 400, 'height': 300, 'fov': 100,
                'id': 'rgb_center'
            },
            {
                'type': 'sensor.camera.rgb',
                'x': 1.3, 'y': 0.0, 'z': 2.3,
                'roll': 0.0, 'pitch': 0.0, 'yaw': -60.0,
                'width': 400, 'height': 300, 'fov': 100,
                'id': 'rgb_left'
            },
            {
                'type': 'sensor.camera.rgb',
                'x': 1.3, 'y': 0.0, 'z': 2.3,
                'roll': 0.0, 'pitch': 0.0, 'yaw': 60.0,
                'width': 400, 'height': 300, 'fov': 100,
                'id': 'rgb_right'
            },
            {
                'type': 'sensor.camera.rgb',
                'x': -1.3, 'y': 0.0, 'z': 2.3,
                'roll': 0.0, 'pitch': 0.0, 'yaw': 180.0,
                'width': 400, 'height': 300, 'fov': 100,
                'id': 'rgb_rear'
            },
            # TO DO: Better to add noise setting to GNSS, IMU and Speedmeter
            {
                'type': 'sensor.other.gnss',
                'x': 0.0, 'y': 0.0, 'z': 0.0,
                'roll': 0.0, 'pitch': 0.0, 'yaw': 0.0,
                'sensor_tick': 0.01,
                'id': 'gps'
            },
            {
                'type': 'sensor.other.imu',
                'x': 0.0, 'y': 0.0, 'z': 0.0,
                'roll': 0.0, 'pitch': 0.0, 'yaw': 0.0,
                'sensor_tick': 0.05,
                'id': 'imu'
            },
            {
                'type': 'sensor.speedometer',
                'reading_frequency': 20,
                'id': 'Speed'
            }
        ]
        return sensors
    
    def run_step(self, input_data, timestamp):
        """
        This method will be called once per time step to produce a new action in the 
        form of a carla.VehicleControl object.
        """
        # control = self._do_something_smart(input_data, timestamp)
        control = carla.VehicleControl()
        control.steer = 3.0
        control.throttle = 10.0
        control.brake = 0.0
        print("timestamp: ", timestamp)
        return control
    
    def destroy(self):
        pass