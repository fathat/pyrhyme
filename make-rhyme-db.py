#!/usr/bin/env python
import sqlite3 as sql

con = sql.connect('data/rhyme.db')

con.execute('drop table words')
con.execute('drop table rhymes')
con.execute('create table words (word, sound, syllables)')
con.execute('create table rhymes (sound, words)')

with open('data/words.csv') as words:
	lines = words.readlines()
	for line in lines:
		word, data = line.lower().split(', ')
		sound, syllables = data.strip().split(' ')
		con.execute('insert into words values (?, ?, ?)',
					(word, sound, syllables))

with open('data/rhymes.csv') as words:
	lines = words.readlines()
	for line in lines:
		sound, words = line.lower().split(', ')
		con.execute('insert into rhymes values (?, ?)',
					(sound.strip(), words.strip()))

con.commit()
con.close()