from datetime import datetime,timedelta
dt = datetime.now() - timedelta(days=5)
print('Current date - ',datetime.now())
print('5 days before current date :',dt)