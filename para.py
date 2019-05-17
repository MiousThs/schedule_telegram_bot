import sqlite3
import time
import config

#list of weeks
chis = {'Mar':[20, 21, 22, 23, 24],
 		'Apr':[1, 2, 3, 4, 5, 6, 7, 15, 16, 17, 18, 19, 20, 21, 29, 30],
 		'May':[1, 2, 3, 4, 5, 13, 14, 15, 16, 17, 18, 19, 27, 28, 29, 30, 31]}

week_days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']

#main class to work with
class Para:
	def __init__(self, database):
		self.connection = sqlite3.connect(config.database_name, check_same_thread=False)
		self.cursor = self.connection.cursor()

	def get_next(self):
		self.current_time = time.asctime()

		for i in chis[self.current_time.split()[1]]:
			if int(self.current_time.split()[2]) == i:
				self.ch_zn = 'ch'
				break
			self.ch_zn = 'zn'

		self.today_day = week_days[int(time.strftime('%w', time.gmtime()))]
		self.current_hour = self.current_time.split()[3].split(':')[0]
		self.current_minute = self.current_time.split()[3].split(':')[1]

		try:
			if self.ch_zn == 'ch':
				b = self.cursor.execute('SELECT * FROM rozkl WHERE day="{0}" AND ch="1" AND hour>="{1}"'.format(self.today_day, self.current_hour)).fetchall()[0]
			else:
				b = self.cursor.execute('SELECT * FROM rozkl WHERE day="{0}" AND zn="1" AND hour>="{1}"'.format(self.today_day, self.current_hour)).fetchall()[0]
			c = []
			if int(b[4]) < 9:
				c.append('Пара: {0}\nАудиторія: {1}\nВикладач: {2}\nЧас: {3}:0{4}\n'.format(b[1], b[8], b[5], b[3], b[4]))
			else:
				c.append('Пара: {0}\nАудиторія: {1}\nВикладач: {2}\nЧас: {3}:{4}\n'.format(b[1], b[8], b[5], b[3], b[4]))
			return c
		except:
			return 'Здається вже нічого нема сьогодні\nНу а завтра...\n'+self.get_tomorrow()

	def get_today(self):
		self.current_time = time.asctime()

		for i in chis[self.current_time.split()[1]]:
			if int(self.current_time.split()[2]) == i:
				self.ch_zn = 'ch'
				break
			self.ch_zn = 'zn'

		today_day = week_days[int(time.strftime('%w', time.gmtime()))]
		if today_day == 'sat':
			return 'Сьогодні субота. Які пари???'
		elif today_day == 'sun':
			return 'Сьогодні неділя. Пари тільки завтра.'

		if self.ch_zn == 'ch':
			b = self.cursor.execute('SELECT * FROM rozkl WHERE day="{0}" AND ch="1"'.format(today_day)).fetchall()
		else:
			b = self.cursor.execute('SELECT * FROM rozkl WHERE day="{0}" AND zn="1"'.format(today_day)).fetchall()
		c = []
		cnt = 0

		for i in b:
			if int(i[4]) < 9:
				c.append('Пара: {0}\nАудиторія: {1}\nВикладач: {2}\nЧас: {3}:0{4}\n'.format(i[1], i[8], i[5], i[3], i[4]))
			else:
				c.append('Пара: {0}\nАудиторія: {1}\nВикладач: {2}\nЧас: {3}:{4}\n'.format(i[1], i[8], i[5], i[3], i[4]))
			cnt+=1

		answ = ''
		for i in range(cnt):
			answ+=c[i]

		return answ

	def get_tomorrow(self):
		self.current_time = time.asctime()
		for i in chis[self.current_time.split()[1]]:
			if int(self.current_time.split()[2])+1 == i:
				self.ch_zn = 'ch'
				break
			self.ch_zn = 'zn'
		today_day = week_days[int(time.strftime('%w', time.gmtime()))+1]
		if today_day == 'sat':
			return 'Нарешті субота...'
		elif today_day == 'sun':
			return 'Завтра неділя.'		
		if self.ch_zn == 'ch':
			b = self.cursor.execute('SELECT * FROM rozkl WHERE day="{0}" AND ch="1"'.format(today_day)).fetchall()
		else:
			b = self.cursor.execute('SELECT * FROM rozkl WHERE day="{0}" AND zn="1"'.format(today_day)).fetchall()
		c = []
		cnt = 0
		for i in b:
			if int(i[4]) < 9:
				c.append('Пара: {0}\nАудиторія: {1}\nВикладач: {2}\nЧас: {3}:0{4}\n'.format(i[1], i[8], i[5], i[3], i[4]))
			else:
				c.append('Пара: {0}\nАудиторія: {1}\nВикладач: {2}\nЧас: {3}:{4}\n'.format(i[1], i[8], i[5], i[3], i[4]))
			cnt+=1
		answ = ''
		for i in range(cnt):
			answ+=c[i]
		return answ

	def get_week(self):
		self.current_time = time.asctime()

		for i in chis[self.current_time.split()[1]]:
			if int(self.current_time.split()[2]) == i:
				self.ch_zn = 'ch'
				break
			self.ch_zn = 'zn'

		if self.ch_zn == 'ch':
			return 'Вроді чисельник'
			
		else:
			return 'Ніби знаменник'