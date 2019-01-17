class Solution(object):
    def __init__(self):
		# the underlying read4 function will remember the position in the file therefore we need to use a global cache
        self.queue = []
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """   
		# I have referred to other python solutions in the forum
		# If we deduct the number of remaining characters in our global buffer first we can save a call to read4 since that way the while loop won't execute
        N = n - len(self.queue)
        buf4 = ['']*4
		# we just keep reading until we've read all required characters or reached the end of the file
        while N > 0:
            k = read4(buf4)
            if k == 0:
                break
            self.queue.extend(buf4[:k])
            N -= k
		# after we finish reading all characters, we write to buf in one go
		# however, since OJ will use the old list instance, we can only operate on the original list
		# I guess OJ added an empty string to the original buf hence you need to delete all items first before extend
        del buf[:] 
        buf.extend([self.queue.pop(0) for _ in xrange(min(len(self.queue), n))])
		# we can also use the the slice assignment in one line as follows
        # buf[0:] = [self.queue.pop(0) for _ in xrange(min(len(self.queue), n))]
        return len(buf)