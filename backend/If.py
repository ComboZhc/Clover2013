import sqlite3
from DbUtils import *

from triggers import *
'''
HANDLER(trigger_info, user_info)
return pending_info(to be logged into db) if ok
else return None
'''
HANDLERS = {
	'mail-new': FudanMailTrigger.test, 
	'weibo-new': WeiboTrigger.test, 
	'renren-new': RenrenTrigger.test
	}

def run():
	for task in execute('select * from app_task'):
		task_info = dict(zip(APP_TASK, task))
		user_info = fetchById('auth_user', task_info['user_id']) 
		trigger_info = fetchById('app_trigger', task_info['trigger_id'])
		action_info = fetchById('app_action', task_info['action_id'])

		pending_info = HANDLERS[trigger_info['kind']](trigger_info, user_info)
		
		if pending_info != None:
			insert('app_pending', pending_info)
		execute("update app_trigger set updated_at = datetime('now') where id = %s" % task_info['id'])
	con.commit()	

if __name__ == '__main__':
	pass