import json
import os
import numpy as np

class TVCModel:
    def __init__(self, design_file=None):
        self.design_file = design_file
        self.load_design()

    def load_design(self): # Load the design parameters from the JSON file
        self.design_params = {}
        if self.design_file is None:
            print("Design file not specified. Generating example...")
            self.create_example_design_file()
            return
        try:
            with open(self.design_file, 'r') as f:
                self.design_params = json.load(f)
        except FileNotFoundError:
            self.design_params = {}
            print(f"Design file {self.design_file} not found. Exiting...")
            exit(1)
        except json.JSONDecodeError:
            self.design_params = {}
            print(f"Error decoding JSON from design file {self.design_file}. Exiting...")
            exit(1)

    def get_design_parameters(self): #return the design parameters
        return self.design_params

    def set_design_parameters(self, params):
        self.design_params = params
        self.save_design()

    def save_design(self): # Save the design parameters to the JSON file
        
        with open(self.design_file, 'w') as f:
            json.dump(self.design_params, f)

    def create_example_design_file(self): #generate example design file
        self.design_params = {
            "L1": 100,
            "L2": 200,
            "L3": 300,
            "S2_x": 50,
            "S2_y": 75
        }

        with open("design.json", 'w') as f:
            json.dump(self.design_params, f)

    def circle_intersect(self, x0, y0, r0, x1, y1, r1): #code from https://www.johndcook.com/blog/2023/08/27/intersect-circles/
            c0 = np.array([x0, y0])
            c1 = np.array([x1, y1])
            v = c1 - c0
            d = np.linalg.norm(v)
        
            if d > r0 + r1 or d == 0:
                return None
            
            u = v/np.linalg.norm(v)
            xvec = c0 + (d**2 - r1**2 + r0**2)*u/(2*d)
        
            uperp = np.array([u[1], -u[0]])
            a = ((-d+r1-r0)*(-d-r1+r0)*(-d+r1+r0)*(d+r1+r0))**0.5/d
            intersections = (xvec + a*uperp/2, xvec - a*uperp/2)
            return intersections

    def set_relation(self, theta_min, theta_max, alpha_min, alpha_max):
        self.relation = {
            "theta_min": theta_min,
            "theta_max": theta_max,
            "alpha_min": alpha_min,
            "alpha_max": alpha_max
        }
        self.points = 100 #amount of discrete values

        self.theta_values_relation = np.linspace(self.relation["theta_min"], self.relation["theta_max"], self.points)
        self.alpha_values_relation = np.linspace(self.relation["alpha_min"], self.relation["alpha_max"], self.points)

    def simulate_kinematics(self): #calculate kinematics of the mount
        if not hasattr(self, 'relation'):
            print("Relation not set. Please set the relation first.")
            return

        L1 = self.design_params.get('L1', 0)
        L2 = self.design_params.get('L2', 0)
        L3 = self.design_params.get('L3', 0)

        x3 = self.design_params.get('S2_x', 0)
        y3 = self.design_params.get('S2_y', 0)

        #calculate ranges of theta and alpha
        theta_range = self.theta_values_relation
        alpha_range = []

        x2, y2 = None, None #initialize x2 and y2

        #loop over all the theta angles to find the corresponding alpha angles
        for theta in theta_range:
            x1 = L1 * np.sin(np.radians(theta))
            y1 = L1 * np.cos(np.radians(theta))

            intersections = self.circle_intersect(x1, y1, L2, x3, y3, L3) #calculate intersections
            if intersections is not None: #take intersection with lowest y values
                if intersections[0][1] < intersections[1][1]:
                    x2, y2 = intersections[0]
                else:
                    x2, y2 = intersections[1]

            if x2 is not None and y2 is not None:
                alpha_range.append(np.degrees(np.arcsin((x2 - x3) / L3)))
            else:
                alpha_range.append(None)

        # Store the calculated alpha range
        self.alpha_values_simulated = alpha_range.copy()

    def plot_results(self):
        import matplotlib.pyplot as plt
        if not hasattr(self, 'alpha_values_simulated'):
            print("Alpha values not simulated yet, try simulate_kinematics()")
            return

        # Plot the simulated alpha values
        plt.plot(self.theta_values_relation, self.alpha_values_relation, label='Desired relation', color='blue', linestyle='--')
        plt.plot(self.theta_values_relation, self.alpha_values_simulated, label='Simulated relation', color='red')
        plt.xlabel('Theta (degrees)')
        plt.ylabel('Alpha (degrees)')
        plt.title('Simulated Alpha vs Theta')
        plt.grid()
        plt.legend()
        plt.show()

