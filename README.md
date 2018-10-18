## Haircut Scheduling App

### Purpose
I submitted this for an assignment a few years ago.
I still like Python, and still identify with the general way that I approached this exercise, so uploading it for record-keeping's sake.


#### Files
`scheduler.py` - main file and class, contains methods which invoke model classes and methods. Contains the command line interface.

`dailyschedule.py` - model (DailySchedule class) for one day's schedule. Contains a list of Slots.

`slot.py` - model (Slot class) for one 15-minute appointment slot.

#### How to run
`python3 scheduler.py`
(No additional parameters in the command. Follow resulting prompts.)

## Test Console Output

```
kirien@stardust-tapestry~/haircut-scheduler$ python3 scheduler.py
Welcome to Haircut Scheduler. Options: 
[1] to list all appointments.
[2] to schedule an appointment.
[3] to exit the program.
1
No appointments have been scheduled.

Welcome to Haircut Scheduler. Options: 
[1] to list all appointments.
[2] to schedule an appointment.
[3] to exit the program.
2
Enter appointment date in the format (MM DD YYYY): 09 30 2015
Enter appointment time in 24hr format (HH:MM): 9:00
Enter appointment name: Early
Enter "HC" for Haircut, "HCS" for Shampoo + Haircut: HC
Appointment scheduled.
Welcome to Haircut Scheduler. Options: 
[1] to list all appointments.
[2] to schedule an appointment.
[3] to exit the program.
1
Appointments for: Sep 30 2015

09:00:00 - Early, Haircut
09:15:00 - Early, Haircut
---------------------------

Welcome to Haircut Scheduler. Options: 
[1] to list all appointments.
[2] to schedule an appointment.
[3] to exit the program.
2
Enter appointment date in the format (MM DD YYYY): 10 01 2015
Enter appointment time in 24hr format (HH:MM): 16:45
Enter appointment name: Too Late
Enter "HC" for Haircut, "HCS" for Shampoo + Haircut: HC
Appointment time not available. Please try a different time.
Welcome to Haircut Scheduler. Options: 
[1] to list all appointments.
[2] to schedule an appointment.
[3] to exit the program.
2
Enter appointment date in the format (MM DD YYYY): 10 01 2015
Enter appointment time in 24hr format (HH:MM): 16:30
Enter appointment name: Late Haircut
Enter "HC" for Haircut, "HCS" for Shampoo + Haircut: HC
Appointment scheduled.
Welcome to Haircut Scheduler. Options: 
[1] to list all appointments.
[2] to schedule an appointment.
[3] to exit the program.
1
Appointments for: Sep 30 2015

09:00:00 - Early, Haircut
09:15:00 - Early, Haircut
---------------------------

Appointments for: Oct 01 2015

16:30:00 - Late Haircut, Haircut
16:45:00 - Late Haircut, Haircut
---------------------------

Welcome to Haircut Scheduler. Options: 
[1] to list all appointments.
[2] to schedule an appointment.
[3] to exit the program.
2
Enter appointment date in the format (MM DD YYYY): 10 02 2015
Enter appointment time in 24hr format (HH:MM): 12:30
Enter appointment name: Long Appointment
Enter "HC" for Haircut, "HCS" for Shampoo + Haircut: HCS
Appointment scheduled.
Welcome to Haircut Scheduler. Options: 
[1] to list all appointments.
[2] to schedule an appointment.
[3] to exit the program.
1
Appointments for: Sep 30 2015

09:00:00 - Early, Haircut
09:15:00 - Early, Haircut
---------------------------

Appointments for: Oct 01 2015

16:30:00 - Late Haircut, Haircut
16:45:00 - Late Haircut, Haircut
---------------------------

Appointments for: Oct 02 2015

12:30:00 - Long Appointment, Shampoo + Haircut
12:45:00 - Long Appointment, Shampoo + Haircut
13:00:00 - Long Appointment, Shampoo + Haircut
13:15:00 - Long Appointment, Shampoo + Haircut
---------------------------

Welcome to Haircut Scheduler. Options: 
[1] to list all appointments.
[2] to schedule an appointment.
[3] to exit the program.
3
Exiting. No information will be saved.
```
