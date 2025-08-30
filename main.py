from TVCModel import TVCModel

if __name__ == "__main__":
    design_file = "design.json"
    tvc_model = TVCModel(design_file=design_file)
    tvc_model.set_relation(theta_min=-50, theta_max=50, alpha_min=-8, alpha_max=8)

    # L1_values = [5, 10, 15, 20]
    # for L1 in L1_values:
    #     tvc_model.set_L1(L1)
    #     tvc_model.simulate_kinematics()
    #     tvc_model.add_plot_results(x_data=tvc_model.theta_values_relation, y_data=tvc_model.alpha_values_simulated, label=f"L1 = {L1}")
    # tvc_model.show_plot()

    # L2_values = [10, 20, 30, 40, 50]
    # for L2 in L2_values:
    #     tvc_model.set_L2(L2)
    #     tvc_model.simulate_kinematics()
    #     tvc_model.add_plot_results(x_data=tvc_model.theta_values_relation, y_data=tvc_model.alpha_values_simulated, label=f"L2 = {L2}")
    # tvc_model.show_plot()

    # L3_values = [20, 30, 40, 50]
    # for L3 in L3_values:
    #     tvc_model.set_L3(L3)
    #     tvc_model.simulate_kinematics()
    #     tvc_model.add_plot_results(x_data=tvc_model.theta_values_relation, y_data=tvc_model.alpha_values_simulated, label=f"L3 = {L3}")
    # tvc_model.show_plot()

    # S2_x_values = [20, 30, 40, 50]
    # for S2_x in S2_x_values:
    #     tvc_model.set_S2_x(S2_x)
    #     tvc_model.simulate_kinematics()
    #     tvc_model.add_plot_results(x_data=tvc_model.theta_values_relation, y_data=tvc_model.alpha_values_simulated, label=f"S2_x = {S2_x}")
    # tvc_model.show_plot()

    S2_y_values = [30, 40, 50, 60]
    for S2_y in S2_y_values:
        tvc_model.set_S2_y(S2_y)
        tvc_model.simulate_kinematics()
        tvc_model.add_plot_results(x_data=tvc_model.theta_values_relation, y_data=tvc_model.alpha_values_simulated, label=f"S2_y = {S2_y}")
    tvc_model.show_plot()
