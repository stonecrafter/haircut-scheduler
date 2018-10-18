#!/bin/python

from datetime import date, time, datetime
from dailyschedule import DailySchedule
from slot import Slot

class Scheduler:
	'''The main class for scheduling haircut appointments.'''

	def __init__(self):
		'''Set up initial values.'''

		# Keys are dates (as datetime objects), values are DailySchedule
		# objects, corresponding to the schedule object for that particular day.
		# Use a dictionary here so it is easy to look up by date.
		self.days = {}

	def list(self):
		'''List all currently scheduled appointments.'''

		# Iterate through all the dates for which appointments have been
		# scheduled, and print them. If no appointments have been scheduled,
		# indicate so.
		if not self.days:
			print('No appointments have been scheduled.\n')
		
		# Sort the dictionary entries by date, so that the appointments
		# can be listed in order.
		for date in sorted(self.days):
			schedule = self.days[date]
			print('Appointments for: ' + schedule.get_day() + '\n')
			schedule.list_appointments()
			print('---------------------------\n')

	def schedule(self):
		'''Schedule an appointment for a specified date and time. Indicate whether or not the scheduling was successful.'''

		scheduled = False
		day = input('Enter appointment date in the format (MM DD YYYY): ')
		formatted_date = datetime.date(datetime.strptime(day, '%m %d %Y'))
		# If there are no appointments scheduled for this day yet, we need to
		# create a new schedule for that day, before we can add in the appointment.
		if formatted_date not in self.days:
			scheduled_day = DailySchedule(formatted_date)
			self.days[formatted_date] = scheduled_day
		else:
			scheduled_day = self.days[formatted_date]

		# Attempt to schedule the appointment
		time = input('Enter appointment time in 24hr format (HH:MM): ')
		name = input('Enter appointment name: ')
		appt_type = input('Enter "HC" for Haircut, "HCS" for Shampoo + Haircut: ')
		formatted_time = datetime.time(datetime.strptime(time, '%H:%M'))
		# This function will return True if appointment was successfully scheduled, False if not.
		scheduled = scheduled_day.schedule_appointment(formatted_time, name, appt_type)
		
		# Check result
		if scheduled:
			print('Appointment scheduled.')
		else:
			print('Appointment time not available. Please try a different time.')


if __name__ == '__main__':

	scheduler = Scheduler()

	while True:
		option = int(input('Welcome to Haircut Scheduler. Options: \n[1] to list all appointments.\n[2] to schedule an appointment.\n[3] to exit the program.\n'))
		if option == 1:
			scheduler.list()
		elif option == 2:
			scheduler.schedule()
		elif option == 3:
			print('Exiting. No information will be saved.')
			exit()
		else:
			print("Invalid option. Please try again.\n")
