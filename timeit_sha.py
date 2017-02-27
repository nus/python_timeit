#coding: utf-8
import timeit
import hashlib

print 'SHA1\t', timeit.timeit("hashlib.sha1('').hexdigest()", 'import hashlib', number=1000000)
print 'SHA256\t', timeit.timeit("hashlib.sha256('').hexdigest()", 'import hashlib', number=1000000)
print 'SHA512\t', timeit.timeit("hashlib.sha512('').hexdigest()", 'import hashlib', number=1000000)
