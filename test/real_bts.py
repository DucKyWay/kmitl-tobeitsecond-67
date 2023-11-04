N8_E9_W1_S6_fares = [0, 17, 25, 28, 32, 40, 43, 47]
BMA_flat_fare = 15
free_service_stations = ['E14', 'E15', 'E16', 'E17', 'E18', 'E19', 'E20', 'E21', 'E22', 'E23', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19', 'N20', 'N21', 'N22', 'N23', 'N24']
free_N = ['N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19', 'N20', 'N21', 'N22', 'N23', 'N24']
free_E = ['E14', 'E15', 'E16', 'E17', 'E18', 'E19', 'E20', 'E21', 'E22', 'E23']

free_stage = 

def calculate_fare(entrance, terminal):
    if entrance == "N6" or terminal == "N6":
        return "Error"

    if entrance in free_N and terminal in free_N or \
       entrance in free_E and terminal in free_E:
        return 0
    
    main_fare = 0
    if "N" in entrance and "E" in terminal or \
       "E" in entrance and "N" in terminal:
        main_fare = max(N8_E9_W1_S6_fares)
    elif "S" in entrance and "W" in terminal or \
         "W" in entrance and "S" in terminal:
        print("test")
    elif "N" in entrance and "W" in terminal or \
         "W" in entrance and "N" in terminal:
        print("test")
    # elif
    bma_fare = 0
    if entrance in free_service_stations and terminal not in free_service_stations or \
       entrance not
        in free_service_stations and terminal in free_service_stations:
        bma_fare = BMA_flat_fare

    total_fare = main_fare + bma_fare

    if entrance in free_service_stations or terminal in free_service_stations:
        total_fare += BMA_flat_fare
    
    return total_fare

entrance, terminal = input(), input()
fare = calculate_fare(entrance, terminal)
print(fare)
