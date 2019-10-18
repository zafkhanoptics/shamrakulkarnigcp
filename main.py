import webapp2


class arun(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Sharma And Kulkarni welcome you abode the DBDA Express !!!!')


app = webapp2.WSGIApplication([
    ('/', arun),
], debug=True)
