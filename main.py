from TVCModel import TVCModel

if __name__ == "__main__":
    design_file = "design.json"
    tvc_model = TVCModel(design_file=design_file)
    tvc_model.set_relation(theta_min=-30, theta_max=30, alpha_min=-8, alpha_max=8)

    tvc_model.optimize(10,50,10,50,25)
    tvc_model.plot_heatmap()