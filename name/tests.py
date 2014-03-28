from django.test import TestCase

from name.models import Parser


class ParserTests(TestCase):
	def test_filter_drm_none(self):
		parser = Parser()
		result = parser.filter_drm(None)
		self.assertEqual([], result)


	def test_filter_drm_empty(self):
		parser = Parser()
		result = parser.filter_drm([])
		self.assertEqual([], result)


	def test_filter_drm_missing(self):
		parser = Parser()
		
		payload = [
			{
			},
		]
		
		result = parser.filter_drm(payload)
		self.assertEqual([], result)

	def test_filter_drm_false(self):
		parser = Parser()
		
		payload = [
			{
				"drm": False,
			},
		]
		
		result = parser.filter_drm(payload)
		self.assertEqual([], result)


	def test_filter_drm_true(self):
		parser = Parser()
		
		payload = [
			{
				"drm": True,
			},
		]
		
		result = parser.filter_drm(payload)
		self.assertEqual(1, len(result))


	def test_filter_episode_none(self):
		parser = Parser()
		result = parser.filter_episode_count(None)
		self.assertEqual([], result)


	def test_filter_episode_empty(self):
		parser = Parser()
		result = parser.filter_episode_count([])
		self.assertEqual([], result)


	def test_filter_episode_missing(self):
		parser = Parser()
		
		payload = [
			{
			},
		]
		
		result = parser.filter_episode_count(payload)
		self.assertEqual([], result)


	def test_filter_episode_zero(self):
		parser = Parser()
		
		payload = [
			{
				"episodeCount": 0,
			},
		]
		
		result = parser.filter_episode_count(payload)
		self.assertEqual([], result)


	def test_filter_episode_one(self):
		parser = Parser()
		
		payload = [
			{
				"episodeCount": 1,
			},
		]
		
		result = parser.filter_episode_count(payload)
		self.assertEqual(1, len(result))


	def test_filter_episode_high(self):
		parser = Parser()
		
		payload = [
			{
				"episodeCount": 1000000,
			},
		]
		
		result = parser.filter_episode_count(payload)
		self.assertEqual(1, len(result))


	def test_format_return_none(self):
		parser = Parser()
		
		result = parser.format_return(None)
		self.assertEqual({"response": []}, result)


	def test_format_return_empty(self):
		parser = Parser()
		
		result = parser.format_return([])
		self.assertEqual({"response": []}, result)


	def test_format_return_single(self):
		parser = Parser()
		
		payload = [
			{
				"image": {
					"showImage": "http://catchup.ninemsn.com.au/img/jump-in/shows/16KidsandCounting1280.jpg",
				},
				"slug": "show/16kidsandcounting",
				"title": "16 Kids and Counting",
			},
		]
		
		result = parser.format_return(payload)
		self.assertEqual(1, len(result))
		self.assertEqual(3, len(result['response'][0]))


	def test_format_return_missing_title(self):
		parser = Parser()
		
		payload = [
			{
				"image": {
					"showImage": "http://catchup.ninemsn.com.au/img/jump-in/shows/16KidsandCounting1280.jpg",
				},
				"slug": "show/16kidsandcounting",
			},
		]
		
		result = parser.format_return(payload)
		self.assertEqual({"response": []}, result)


	def test_format_return_missing_slug(self):
		parser = Parser()
		
		payload = [
			{
				"image": {
					"showImage": "http://catchup.ninemsn.com.au/img/jump-in/shows/16KidsandCounting1280.jpg",
				},
				"title": "16 Kids and Counting",
			},
		]
		
		result = parser.format_return(payload)
		self.assertEqual({"response": []}, result)


	def test_format_return_missing_image(self):
		parser = Parser()
		
		payload = [
			{
				"title": "16 Kids and Counting",
				"slug": "show/16kidsandcounting",
			},
		]
		
		result = parser.format_return(payload)
		self.assertEqual({"response": []}, result)
		
	def test_parse_json_integration(self):
		parser = Parser()
		
		payload = { "payload": [
			{
				"drm": True,
				"episodeCount": 3,
				"image": {
					"showImage": "http://catchup.ninemsn.com.au/img/jump-in/shows/16KidsandCounting1280.jpg",
				},
				"title": "16 Kids and Counting",
				"slug": "show/16kidsandcounting",
			},
		]}
		
		result = parser.parse_json(payload)
		self.assertEqual(1, len(result))
