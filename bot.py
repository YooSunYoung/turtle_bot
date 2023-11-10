# SPDX-License-Identifier: BSD-3-Clause

# flake8: noqa F401

import numpy as np

from vendeeglobe import (
    Checkpoint,
    Heading,
    Instructions,
    Location,
    MapProxy,
    Vector,
    WeatherForecast,
    config,
)
from vendeeglobe.utils import distance_on_surface

CREATOR = "NewSun"  # This is your team name


class Bot:
    """
    This is the ship-controlling bot that will be instantiated for the competition.
    """

    def __init__(self):
        from pathlib import Path
        self.team = CREATOR  # Mandatory attribute
        self.avatar = str(Path(__file__).parent / Path("turtle.png"))  # Optional attribute
        self.course = [
            Checkpoint(latitude=47.259668, longitude=-12.307703, radius=50),
            Checkpoint(latitude=58.242263, longitude=-50.246452, radius=50),
            Checkpoint(latitude=74.369396, longitude=-63.317311, radius=50),
            Checkpoint(latitude=74.243486, longitude=-78.445666, radius=50),
            Checkpoint(latitude=74.137806, longitude=-88.763979, radius=50), 
            Checkpoint(latitude=74.285566, longitude=-96.211784, radius=50), 
            Checkpoint(latitude=74.484131, longitude=-98.880967, radius=50),
            Checkpoint(latitude=74.348479, longitude=-107.717569, radius=50),
            Checkpoint(latitude=73.784153, longitude=-111.685024, radius=50), 
        
            Checkpoint(latitude=73.799267, longitude=-113.872269, radius=50), 
            Checkpoint(latitude=75.059851, longitude=-123.269867, radius=15), 
            Checkpoint(latitude=74.425129, longitude=-126.274171, radius=5),
            Checkpoint(latitude=71.108255, longitude=-128.696315, radius=50),
            Checkpoint(latitude=69.858095, longitude=-136.182943, radius=50), 
            Checkpoint(latitude=70.262470, longitude=-141.180715, radius=50),
            Checkpoint(latitude=70.361510, longitude=-142.856392, radius=50), 
            Checkpoint(latitude=70.582164, longitude= -147.732131, radius=50),
            Checkpoint(latitude=70.746083, longitude=-149.286656, radius=50), 


            Checkpoint(latitude=71.707721, longitude=-156.545591, radius=50), 
            Checkpoint(latitude=69.414574, longitude=-169.977017, radius=15), 
            Checkpoint(latitude=66.070089, longitude=-168.394463, radius=50), 
            Checkpoint(latitude=65.714540, longitude=-168.518280, radius=5),
            Checkpoint(latitude=64.331784, longitude=-168.878476, radius=5),
            Checkpoint(latitude=63.490345, longitude=-166.661021, radius=5),
            Checkpoint(latitude=61.322482, longitude=-168.653354, radius=5),
            Checkpoint(latitude=57.289452, longitude=-170.984819, radius=5),
            Checkpoint(latitude=52.360316, longitude=-171.544929, radius=5),  # Finally out of little islands!
            # Checkpoint(latitude=-8.460766, longitude=-166.424428, radius=50), 
            Checkpoint(latitude=17.850557, longitude=-169.261167, radius=50),# Checkpoint 1
            Checkpoint(latitude=8.705004, longitude=173.375068, radius=50),
            Checkpoint(latitude=4.882734, longitude=173.432531, radius=50),
            Checkpoint(latitude=3.288166, longitude=161.774183, radius=50), 
            Checkpoint(latitude=4.621448, longitude=130.998087, radius=50),
            Checkpoint(latitude=5.069115, longitude= 126.864848, radius=50),
            
            Checkpoint(latitude=1.640280, longitude=122.914325, radius=50), 
            Checkpoint(latitude=2.040850, longitude=119.894179, radius=50),


            Checkpoint(latitude=-3.324410, longitude=117.804409, radius=50),
            Checkpoint(latitude=-8.080066, longitude=116.043850, radius=5),
            Checkpoint(latitude=-8.787996, longitude=115.728954, radius=50), 
            # # Checkpoint(latitude=-8.080066, longitude=116.043850, radius=50),

            # Checkpoint(latitude=-49.316100, longitude= -172.853949, radius=50),
            # Checkpoint(latitude=-49.303267, longitude=120.173395, radius=50),
            # Checkpoint(latitude=-13.831352, longitude=99.649492, radius=50),
            Checkpoint(latitude=-14.311934, longitude=82.143549, radius=50), # Checkpoint 2

            Checkpoint(latitude=-39.095684, longitude=33.919624, radius=50), # Africa
            Checkpoint(latitude=-38.838873, longitude=9.147060, radius=50),
            Checkpoint(latitude=-0.628860, longitude=-1.507954, radius=50),
            Checkpoint(latitude=3.038772, longitude=-20.571164, radius=150),
            Checkpoint(latitude=19.257600, longitude=-33.173621, radius=50),
            Checkpoint(latitude=47.259668, longitude=-12.307703, radius=50),
            Checkpoint(
                latitude=config.start.latitude,
                longitude=config.start.longitude,
                radius=5,
            )
        ]

    def run(
        self,
        t: float,
        dt: float,
        longitude: float,
        latitude: float,
        heading: float,
        speed: float,
        vector: np.ndarray,
        forecast: WeatherForecast,
        world_map: MapProxy,
    ):
        """
        This is the method that will be called at every time step to get the
        instructions for the ship.

        Parameters
        ----------
        t:
            The current time in hours.
        dt:
            The time step in hours.
        longitude:
            The current longitude of the ship.
        latitude:
            The current latitude of the ship.
        heading:
            The current heading of the ship.
        speed:
            The current speed of the ship.
        vector:
            The current heading of the ship, expressed as a vector.
        forecast:
            The weather forecast for the next 5 days.
        world_map:
            The map of the world: 1 for sea, 0 for land.
        """
        instructions = Instructions()
        for ch in self.course:
            dist = distance_on_surface(
                longitude1=longitude,
                latitude1=latitude,
                longitude2=ch.longitude,
                latitude2=ch.latitude,
            )
            instructions.sail = 1.0
            if dist < ch.radius:
                ch.reached = True
            if not ch.reached:
                instructions.location = Location(
                    longitude=ch.longitude, latitude=ch.latitude
                )
                break

        return instructions
