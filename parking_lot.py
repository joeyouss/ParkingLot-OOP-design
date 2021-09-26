# main function where every utility lies

# min heap for getting the nearest slot available since it avoides us from sorting again and again
import heapq as nearest_slot
from collections import defaultdict, OrderedDict

class Car:
    def __init__(self, reg_no, driver_age):
      '''
      This function initializes the car object and verifies that the car is registered
      Arguments : reg_no - registration number of the car, Type: String
              driver_age - age of the driver. Type - Integer
      '''
      self.reg_no = reg_no
      self.age = driver_age    

class ParkingLot:
    # constructor for initalizing data structures for storage of information
    def __init__(self):
        self.registration_slot_mapping = dict()
        self.map_age_with_registration = defaultdict(list)
        self.map_slot_with_registration = OrderedDict()
        self.available_slots = []

    def Create_parking_lot(self, req_slots):
      """
      This function creates a parking lot of the req_slots number of slots
      Arguments : req_slots - number of slots required. Type : integer
      """
      req_slots = int(req_slots)
      for slot in range(1, req_slots+1):
        nearest_slot.heappush(self.available_slots, slot)
      print("Created parking of {} slots".format(req_slots))

    def get_nearest_slot(self):
        """
        This function returns the nearest empty slot. We use a min heap for getting the nearest slot so that we do not need to sort it again and again
        """
        return nearest_slot.heappop(self.available_slots) if self.available_slots else None

    def park(self, car):
        """
        This function is responsible for parking the newly entered car
        Arguments : car : details of the car to be parked. Type : Car object
        """
        slot_no = self.get_nearest_slot()
        if slot_no is None:
            print("Could not find a nearest slot, the parking lot is full")
            return
        else:
          self.map_slot_with_registration[slot_no] = car
          self.registration_slot_mapping[car.reg_no] = slot_no
          self.map_age_with_registration[car.age].append(car.reg_no)
          print("Car with vehicle registration number {} Car with vehicle registration number {}".format(car.reg_no, slot_no))
       

    def leave(self, slot_to_leave):
        """
        This function is reponsible for deleting the instance of the car leaving the parking and hence delete every detail from the data structures
        Argument : slot_to_leave - number of slot to be left. Type - Integer
        """
        reg_no = ""
        for registration_no, slot in self.registration_slot_mapping.items():
            if slot == slot_to_leave:
                reg_no = registration_no

        
        if reg_no:
            get_car= self.map_slot_with_registration[slot_to_leave].age
            
            nearest_slot.heappush(self.available_slots, slot_to_leave)
            del self.registration_slot_mapping[reg_no]

            car_to_leave = self.map_slot_with_registration[slot_to_leave]
            self.map_age_with_registration[car_to_leave.age].remove(reg_no)
            del self.map_slot_with_registration[slot_to_leave]
            print("Slot number {} vacated, the car with vehicle registration number {} left the space, the driver of the car was of age {}".format(slot_to_leave, reg_no, get_car ))
            return True
        else:
            print("Slot is already free")
            return False

    def Vehicle_registration_number_for_driver_of_age(self, age):
      """
      Returns the vehicle registration number for the age of driver entered.
      Argument : Age - age of the driver. Type - Integer
      """
      age = int(age)
      registration_numbers = self.map_age_with_registration[age]
      registration_numbers = self.map_age_with_registration[age]
      print(", ".join(registration_numbers))
      

    def Slot_numbers_for_driver_of_age(self, age):
        """
        Fetches the parking slot number for the age of driver entered.
        Argument : Age - age of the driver. Type - Integer
        """
        registration_numbers = self.map_age_with_registration[age]
        slots = [self.registration_slot_mapping[reg_no] for reg_no in registration_numbers]
        print(", ".join(map(str, slots)))
        

    def Slot_number_for_car_with_number(self, registration_number):
        """
        fetches the slot number for a particular reg number 
        Argument : registration_number - the reg number of the car object. Type: string
        """
        slot_number = None
        if registration_number in self.registration_slot_mapping:
            slot_number = self.registration_slot_mapping[registration_number]
            print(slot_number)
           
        else:
            print("No car found with this number")
            
