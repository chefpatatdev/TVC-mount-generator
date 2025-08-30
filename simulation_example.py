#Simulate your TVC mount by creating a design file with your parameters

from TVCModel import TVCModel

if __name__ == "__main__":
    design_file = "design.json"
    tvc_model = TVCModel(design_file=design_file)
    tvc_model.set_relation(theta_min=-30, theta_max=30) #set range of angles to plot
    tvc_model.simulate_kinematics() #simulate the kinematics
    tvc_model.plot_results() #plot the results