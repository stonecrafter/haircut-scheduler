class Slot:
	'''A 15-minute appointment slot.'''

	# Constants for appointment types
	APPT_TYPES = {
		"HC": "Haircut",
		"HCS": "Shampoo + Haircut"
	}

	def __init__(self, time, name='', appt_type=None):
		'''Initialize default values. Time is the start of the 15-minute slot, name is the
		name of the appointment booked in this slot (None if slot is vacant), and appt_type
		represents the type of the appointment (see all possibilities in APPT_TYPES constant).'''

		self.time = time
		self.name = name
		self.appt_type = appt_type

	# Getters and setters
	def get_time(self):
		'''Return a string representation of the 15-minute interval represented
		by this time slot, in 24-hour format. Example: "13:00" '''

		return self.time.strftime('%H:%M')

	def get_name(self):
		'''Get the name of the appointment.'''

		return self.name

	def get_appt_type(self):
		'''Get the type of the appointment. Either Haircut or Shampoo + Haircut.'''

		return self.appt_type

	def set_time(self, time):
		'''Set the 15-minute interval associated with this appointment slot.
		Expects a datetime.time object.'''

		self.time = time

	def set_name(self, name):
		'''Set the name of the appointment booked in this time slot.'''

		self.name = name

	def set_appt_type(self, appt_type):
		'''Set the type of the appointment. Either Haircut (HC) or Shampoo + Haircut (HCS).'''

		self.appt_type = Slot.APPT_TYPES[appt_type]

	def get_appt_info(self):
		'''Return all information about the appointment: Time, Name, Type.'''

		return "{} - {}, {}".format(self.time, self.name, self.appt_type)
