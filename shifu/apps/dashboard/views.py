from flask import url_for,redirect,render_template,request,make_response

from apps.dashboard import dashboard
from apps import nocache
from apps import database

from apps.users import sessions
from apps.users import alert
from apps.pages.db import PagesDAO
from apps.website.db import WebsiteDAO

@dashboard.route('/<username>')
@nocache
def dashboard_home(username):

	if sessions.logged_in(username) is not None:
		
		#data access objects
		obj_pages = PagesDAO(database)
		obj_website = WebsiteDAO(database)

		#get all the pages with all the details
		pages_cur = obj_pages.get_all_pages()
		
		pages = []

		#converting date modified in displayable format
		if pages_cur is not None:
			for page in pages_cur:
				#source
				#df = datetime.now()
				#df.strftime("%d %B %Y %I:%M%p")
				#result = '28 November 2014 06:31PM'
				
				time = page['datemodified']
				page['datemodified'] = time.strftime("%d %B %Y %I:%M%p")
				pages.append(page)
				

		#get website name
		website_name = obj_website.get_website_name() or "Website"

		resp = make_response(render_template('dashboard-home.html',username=username,alert=alert.get_alert(),website_name=website_name,pages=pages))
		alert.reset()
		return resp
	else: 
		#return render_template('errors/401.html',message="invalid user,access denied"),401
		alert.error('Make sure to Log In')
		return redirect( url_for('.admin') )


'''
@dashboard.route('/theme/list')
def themes():
	theme_dir = './apps/static/themes/'
	theme_list = []
	response = ""

	for item in os.listdir(theme_dir):
		if os.path.isdir(os.path.join(theme_dir,item)):
			theme_list.append(item)

	for item in theme_list:
		theme = os.path.join(theme_dir,item)	# path of theme directory
		try:
			manifest = open(os.path.join(theme,'manifest.json'))
			data = json.load(manifest)
			if 'theme-name' in data:
				response += "Theme name : %s" % data['theme-name']
			if 'author' in data:
				response += "author : %s" % data['author']
			manifest.close()
		except IOError:
			pass

	return %s % response
'''
