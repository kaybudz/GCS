import serial

# will most likely have to change everything to self. for the lists and the calls to the lists when implemented into the code unless 
# you can figure out how to call this function in your normal code
team_list = []
mission_list = []
packet_list = []
sw_list = []
pl_list = []
altitude_list = []
temperature_list = []
voltage_list = []
latitude_list = []
longitude_list = []
roll_list = []
pitch_list = []
yaw_list = []
pressure_list = []
speed_list = []


# def update_information(port, rate):
#     print('function is running')
#     with serial.Serial(port, rate, timeout = 4) as ser:
#         while True:
#             print('xbee is connected')
            
#             data = ser.readline().decode('UTF-8', errors='ignore').strip()
#             if data is not None:
#                 print("there is a line")
#                 ## code to turn data into a data list when read from the serial port
#                 #data_string = str(data)
#                 #data_list = data_string.split(',')
#                 #print(data_list)

#                 # fake data list to make sure things append properly
#                 data_list = [0,1,2,3,4,5,6,7,8,9,10,11,12]
#                 if len(data_list) >= 13:
#                     team_list.append(data_list[0])
#                     mission_list.append(data_list[1])
#                     packet_list.append(data_list[2])
#                     sw_list.append(data_list[3])
#                     pl_list.append(data_list[4])
#                     altitude_list.append(data_list[5])
#                     temperature_list.append(data_list[6])
#                     voltage_list.append(data_list[7])
#                     latitude_list.append(data_list[8])
#                     longitude_list.append(data_list[9])
#                     roll_list.append(data_list[10])
#                     pitch_list.append(data_list[11])
#                     yaw_list.append(data_list[12])

#                     print(team_list)
#                     print(mission_list)
#                     print(packet_list)
#                     print(sw_list)
#                     print(pl_list)
#                     print(altitude_list)
#                     print(temperature_list)
#                     print(voltage_list)
#                     print(latitude_list)
#                     print(longitude_list)
#                     print(roll_list)
#                     print(pitch_list)
#                     print(yaw_list)

def update_information():
        #print('function is running')
        with serial.Serial('COM18', 9600, timeout = 2) as ser:
            #if ser.in_waiting: # this may not work but comment back in when we test with actual data
            while True: # add button to toggle starting and stopping reading from the serial port
                data = ser.readline().decode('UTF-8', errors='ignore').strip()
                print(data)
                # getting information into a single list
                if data is not None:
                    first_list = data.split(',,')
                    req_list = first_list[0]
                    our_list = first_list[1]
                    data_list = req_list.split(',')
                    extra_list = our_list.split(',')
                    data_list.append(extra_list[0])
                    data_list.append(extra_list[1])
                    print(data_list)

                    # separating main data list into individual lists
                    if len(data_list) >= 15:
                        team_list.append(data_list[0])
                        mission_list.append(data_list[1])
                        packet_list.append(data_list[2])
                        sw_list.append(data_list[3])
                        pl_list.append(data_list[4])
                        altitude_list.append(data_list[5])
                        temperature_list.append(data_list[6])
                        voltage_list.append(data_list[7])
                        latitude_list.append(data_list[8])
                        longitude_list.append(data_list[9])
                        roll_list.append(data_list[10])
                        pitch_list.append(data_list[11])
                        yaw_list.append(data_list[12])
                        pressure_list.append(data_list[13])
                        speed_list.append(data_list[14])

                        print(team_list)
                        print(temperature_list)
                        print(yaw_list)


# calling the function to run
update_information()

            # try:
            #     line = ser.readline().decode('utf-8', errors='ignore').strip()      
            #     # if not line:
            #     #     continue  # skip empty lines

            #     # data_list = line.split(',')
            #     # print(data_list)

            #     # Example: append values if they exist
            #     # if len(data_list) >= 13:
            #     #     team_list.append(data_list[0])
            #     #     mission_list.append(data_list[1])
            #     #     packet_list.append(data_list[2])
            #     #     sw_list.append(data_list[3])
            #     #     pl_list.append(data_list[4])
            #     #     altitude_list.append(data_list[5])
            #     #     temperature_list.append(data_list[6])
            #     #     voltage_list.append(data_list[7])
            #     #     latitude_list.append(data_list[8])
            #     #     longitude_list.append(data_list[9])
            #     #     roll_list.append(data_list[10])
            #     #     pitch_list.append(data_list[11])
            # #     #     yaw_list.append(data_list[12])

            # except Exception as e:
            #     print(f"Error reading line: {e}")

# print(roll_list)

# import serial

# team_list = []
# mission_list = []
# packet_list = []
# sw_list = []
# pl_list = []
# altitude_list = []
# temperature_list = []
# voltage_list = []
# latitude_list = []
# longitude_list = []
# roll_list = []
# pitch_list = []
# yaw_list = []

# def update_information():
#     data = serial.Serial(port = 'COM13', baudrate = 9600, timeout = 4)
#     while True:
#         data_read = data.readline().decode('utf-8')
#         data_string = str(data_read)
#         data_list = data_string.split(',')
#         # figure out how to get list to update graphs and table
#         print(data_list)

#         # team_list.append(data_list[0])
#         # mission_list.append(data_list[1])
#         # packet_list.append(data_list[2])
#         # sw_list.append(data_list[3])
#         # pl_list.append(data_list[4])
#         # altitude_list.append(data_list[5])
#         # temperature_list.append(data_list[6])
#         # voltage_list.append(data_list[7])
#         # latitude_list.append(data_list[8])
#         # longitude_list.append(data_list[9])
#         # roll_list.append(data_list[10])
#         # pitch_list.append(data_list[11])
#         # yaw_list.append(data_list[12])

#         # print(team_list)
#         # print(packet_list)
#         # print(temperature_list)
#         # print(roll_list)
#         # print(pitch_list)
#         # print(yaw_list)

