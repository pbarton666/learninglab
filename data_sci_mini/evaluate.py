TESTING=True
import math
if TESTING:
    #use a **simple** test database for testing (isolate issue)
    
    #set up db, conn, and curs
    import sqlite3
    connection = sqlite3.connect('mydb')
    cursor = connection.cursor()	

    #create the table needed to test the algorithm
    table="main_voicecall"
    col = "vc.duration_seconds"

    cmd = "DROP TABLE IF EXISTS {}".format(table)
    curs.execute(cmd)    #this runs the SQL command
    conn.commit()        #... and this locks in the changes

    cmd = "CREATE TABLE {} (seconds INT(4))".format(table) 
    curs.execute(cmd)	

    #create a couple iterable objects for seconds and the right answers
    #   this makes testing very transparent
    secs=    [0, 15, 30, 35, 50, 75, 90, None]
    answers= [0, 30, 30, 45, 60, 75, 90, None]

    #add rows, one for each time to be tested
    for test_time in secs:
        cmd="INSERT INTO {} ({}) VALUES ({},)".format(
            table, col, test_time)
    curs.execute(cmd)
    conn.commit()

    #grab the rows
    cmd="SELECT * FROM {}".format(table)
    curs.execute(cmd)

else:	
    #we're NOT testing with sample database
    import psycopg2
    import peek_a_boo
    hostname = peek_a_boo.hostname
    username = peek_a_boo.username
    password = peek_a_boo.password
    database = peek_a_boo.database
    portnum = peek_a_boo.portnum
    seconds = []
    #dur_sum = []
    #start_date = input("Start Date Format yyyy-mm-dd: " + str())
    #end_date = input("End Date Format yyyy-mm-dd: " + str())
    #eid = input("Enterprise ID: ")
    start_date = str('2017-06-04')
    end_date = str('2017-06-22')
    eid = 182250650270173001
    connection = psycopg2.connect(dbname=database, user=username, password=password, host=hostname, port=portnum)
    cursor = connection.cursor()

    cursor.execute("SELECT vc.duration_seconds \
	FROM main_voicecall as vc \
	JOIN main_extendeduser eu on eu.user_id = vc.user_id \
	join auth_user au on eu.user_id = au.id \
	join main_enterpriseaccount ea on ea.id = eu.enterprise_id \
	where (date_trunc('day', vc.call_initiated_ts) >= '%s' and date_trunc('day', vc.call_initiated_ts) <= '%s')\
	and eu.enterprise_id = %s;" % (start_date, end_date, eid))


###modified / marked up code starts here

##for second in cursor:
##	seconds.append(second[0])
##print(seconds)



def evaluate(sec):
    #put the evaluation in a function - this makes it amenable
    #  to unittesting as an isolated operation when you get to that
    #  point.
    
    #use if, not while when evaluating one thing
    if second:  ##a None object fails this test
        if second <= 30:	#minimum billing is 30 seconds	
            return 30
        #bill in 15 second intervals, rounding up
        return math.ceil(second/15)  #easier than dorking around with %

        
    else: #None object encountered
        return None


#The cursor is a generator object; it does "lazy evaluation" - no real need
# to create a list.  Why?  The list lives in memory, all at once.  The generator
# just provides one value at a time, on demand
total=0 
for second in cursor.fetchall():
    total+=evaluate(second)








sec = seconds
se = list(filter(None.__ne__, sec))
print(se)
for s in se:
    while s < 30:
        s = s + 1
    while s % 15 != 0:
        s = s + 1
    print(s)
    number_string = str(s)
    number_list = [0]
    print(sum(map(int, number_string)))
    #things = [list(str(s))]
    #things[:] = [sum(i) for i in zip(things, str(s))]
    #print(things)
    #s = list(str(s))
    #print(s)
    #print(sum(map(int, s)))

    #dur_sum = s
#for thing in s:
    #dur_sum.append(thing[0])
    #print(dur_sum)
    #total = 0
#for thing in s:
#    total = total + thing
#    dur_sum.append(str(thing))
#    print(total)


cursor.close()
connection.close()