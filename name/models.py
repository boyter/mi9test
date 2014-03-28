from django.db import models

class Parser():
	
	def parse_json(self, data):
		filtered = self.filter_drm(data['payload'])
		filtered = self.filter_episode_count(filtered)
		
		return self.format_return(filtered)
	
	def filter_drm(self, data):
		if data is None or data == []:
			return []
		
		result = [x for x in data if 'drm' in x and x['drm'] == True]
		return result

	def filter_episode_count(self, data, count=0):
		if data is None or data == []:
			return []
		
		result = [x for x in data if 'episodeCount' in x and x['episodeCount'] > count]
		return result

	def format_return(self, data):
		if data is None or data == []:
			return {"response": []}
		
		result = [{	"image": x['image']['showImage'], 
					"slug": x['slug'],
					"title": x['title']} for x in data 
					if 'image' in x and 'slug' in x and 'title' in x]
		return {"response": result}
