#An abstract base class with a non-public _Map_Entry class
class BaseMap():

	#nested non-public class
	class _Map_Entry:

		def __init__(self, k, v):
			self._key = k
			self._value = v
		pass

		#compare items based on the keys to see if they are equal
		def __eq__(self, other):
			return self._key == other._key
		pass

		#opposite of __eq__ function
		def __ne__(self, other):
			return not (self._key == other._key)
		pass

		#compare items based on their keys to see if one is less than the other_key
		def __lt__(self, other):
			return self._key < other._key
		pass

		#returns string of key value pair formatted as (key, value)
		def __str__(self):
			s = "(" +str(self._key)+ " : " +str(self._value)+ ")"
			return s
		pass