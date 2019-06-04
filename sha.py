
import hashlib as hl

def hash_value(value):
	return hl.sha256(str(value).encode()).hexdigest()


