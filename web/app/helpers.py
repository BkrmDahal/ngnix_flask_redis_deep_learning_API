"""Helper funcation for preprocessing"""

import numpy as np
import base64
import sys

def base64_encode_image(a):
	"""
	Base64 encode the input NumPy array

	Args:
		a:``array``
			Numpy Array
	
	Returns:
		Numpay array iecode into ``uft-8``
	"""

	return base64.b64encode(a).decode("utf-8")

def base64_decode_image(a, dtype, shape):
	"""
	Convert the string to a NumPy array using the supplied data
	type and target shape

	Args:
		a:``array``
			Numpy Array
		dtype:``np.type``
			np.type to convert too
		shape:``array``
			shape of output

	Returns:
		Reshaped and encode image
	"""
	# if this is Python 3, we need the extra step of encoding the
	# serialized NumPy string as a byte object
	if sys.version_info.major == 3:
		a = bytes(a, encoding="utf-8")

	a = np.frombuffer(base64.decodestring(a), dtype=dtype)
	a = a.reshape(shape)

	# return the decoded image
	return a