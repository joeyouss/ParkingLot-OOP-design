import fileinput
from parking_lot import ParkingLot, Car
# instance of the parking lot
parking_lot = ParkingLot()

# Error handling for wrong input - input with less parameters than required
class Input_error(Exception):
  def __init__(self, no_of_params, message = "The needed number of parameters is :"):
    self.message = message
    self.no_of_params = no_of_params
    printed_message = self.message+self.no_of_params
    print(printed_message)

def process_input(input_commands):
  '''
  This function processes the entered input an implements error handling for errors in input file
  Input : input_commands - The string entered as command. Type : String
  '''
  # distribute the commands into individual strings
  processed_input_commands = input_commands.strip().split(' ')
  # command will be the the keyword triggering the functions. Eg : Park, Leave, etc.
  command = processed_input_commands[0]
  # COMMAND LIST
  if command == 'Create_parking_lot':
    if len(processed_input_commands) < 2:
      raise Input_error(2)
    else:
      parking_lot.Create_parking_lot(processed_input_commands[1])

  elif command == 'Park':
    if len(processed_input_commands) < 2:
        raise Input_error(4)
    else:
      car_details = Car(processed_input_commands[1], int(processed_input_commands[3]))
      parking_lot.park(car_details)

  elif command == 'Leave':
    if len(processed_input_commands) < 2:
      raise Input_error(2)
    else:
      parking_lot.leave(int(processed_input_commands[1]))
        
  elif command == 'Vehicle_registration_number_for_driver_of_age':
    parking_lot.Vehicle_registration_number_for_driver_of_age(processed_input_commands[1])
    
  elif command == 'Slot_numbers_for_driver_of_age':
    parking_lot.Slot_numbers_for_driver_of_age(int(processed_input_commands[1]))
  
  elif command == 'Slot_number_for_car_with_number':
    parking_lot.Slot_number_for_car_with_number(processed_input_commands[1])
  elif command == 'exit':
        exit(0)
  else:
        raise Exception("Invalid command")


# check for input in inputs.txt
if __name__ == "__main__":
  for command in fileinput.input():
      process_input(command)
