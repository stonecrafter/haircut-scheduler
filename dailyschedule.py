from slot import Slot
from datetime import datetime, time, timedelta

class DailySchedule:
	'''One day's schedule. Consists of a series of 15-minute appointment slots,
	starting from 9AM, ending at 5PM.'''

	def __init__(self, date):
		'''Set up inital values. Date is the date for which this schedule applies.'''
		self.slots = []
		self.date = date

		# Fill self.slots with 32 instances of Slots, starting from 9:00 AM
		# In order to use timedelta, we need the full datetime object,
		# including the date, not just the time.
		curr_time = datetime.combine(self.date, time(9, 0))
		interval = timedelta(minutes=15)
		for i in range(0, 32):
			self.slots.append(Slot(curr_time.time()))
			curr_time = curr_time + interval

	def get_day(self):
		'''Return a string representation of the day that corresponds to this schedule.'''

		return self.date.strftime('%b %d %Y')

	def list_appointments(self):
		'''List all of today's appointments.'''

		for slot in self.slots:
			# Omit slots for which no appointment is scheduled. 
			# If there is no appointment, the name for the slot will be empty.
			if slot.get_name():
				print(slot.get_appt_info())

	def schedule_appointment(self, start_time, name, appt_type):
		'''Schedule a new appointment. Return True if scheduled, False if time requested is not available.
		start_time is when the appointment begins, name is the name of the appointment, and appt_type is
		either "HC" meaning Haircut, or "HCS" meaning Shampoo + Haircut.'''

		# Again, we need to combine the date and time in order to use timedelta
		curr_time = datetime.combine(self.date, start_time)

		# First, check the appointment type so we know how many free slots we'll need
		# If haircut, we only need 2 consecutive empty slots.
		if appt_type == "HC":
			# Check that the slot indicated by the start time, as well as the subsequent
			# next slot, is free.
			end_time = timedelta(minutes=30) + curr_time
			num_slots_required = 2
		elif appt_type == "HCS":
			# If shampoo + haircut, we need 4 consecutive empty slots.
			end_time = timedelta(minutes=60) + curr_time
			num_slots_required = 4
		else:
			print('Invalid appointment type. Please try again and indicate "HC" or "HCS" only.')
			return False
			
		# Retrieve the list of slots for which we'll need to use to schedule this appointment
		required_slots = [slot for slot in self.slots if slot.time >= start_time and slot.time < end_time.time()]

		# If the list is empty, it means the start time specified is outside of the hairdresser's workday.
		if not required_slots:
			return False

		# If we have less than the total required number of slots, this means that one or more of the slots
		# requested fell outside the hairdresser's workday.
		if len(required_slots) != num_slots_required:
			return False

		# Check if any spots are occupied. If so, the appointment can't be booked. We check if the spot
		# is occupied by checking if it has a name associated with it.
		for slot in required_slots:
			if slot.name:
				return False

		# All of the required slots are available. The appointment can be scheduled.
		for slot in required_slots:
			slot.set_name(name)
			slot.set_appt_type(appt_type)

		# If we've made it all the way this far, the appointment booking was successful
		return True
