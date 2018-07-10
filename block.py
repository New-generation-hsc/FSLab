"""
This module define the unix file management
include super block and disk index block
"""
import abc


def print_line(deep, length):
	print(' '* deep * 18, '+', '-'*length, '+', '-' * length, '+', sep='')


def print_index(deep, index, length, char='|', size=0):
	idx_str = str(index)
	rest = length - len(idx_str) - length // 2
	size_str = str(size)
	size_rest = length - len(size_str) - length // 2
	print(' ' * deep * 18, char, ' ' * (length // 2), index, ' ' * rest, char, ' ' * (length // 2), size, ' ' * size_rest, char, sep='')


class Item(object):
	"""
	the fat block item
	"""
	def __init__(self, current, next_idx=-1):
		self._cur = current
		self.next_idx = next_idx
		self._size = 0

	@property
	def current(self):
		return self._cur

	@current.setter
	def current(self, idx):
		self._cur = idx

	@property
	def next(self):
		return self.next_idx

	@next.setter
	def next(self, idx):
		self.next_idx = idx

	@property
	def size(self):
		return self._size

	def set_size(self, size):
		self._size = size

	def __repr__(self):
		return "<{}, {}>".format(self.current, self.next)


class FAT(object):
	"""
	the file management include index and next node
	the last node is -1
	"""

	def __init__(self, size, block_size=512):
		"""
		initialize the fat table, and all block is empty
		"""
		self.nodes = [Item(-1, -1) for _ in range(size)]
		self.max_block_size = block_size

	def next(self, index):
		if index == -1:
			return None
		else:
			return self.nodes[index].next

	def allocate(self):
		"""
		from the fat table, search an empty block, return the block index
		"""
		for idx in range(len(self.nodes)):
			if self.nodes[idx].current == -1:
				self.nodes[idx].current = idx
				return self.nodes[idx]
		return -1

	def link(self, current, next_idx):
		"""
		link the current node and the next node
		"""
		self.nodes[current].next = next_idx

	def display(self, idx):
		"""
		display a file block in the console
		"""
		if idx is None or idx == -1:
			return
		print_line(0, 16)
		while idx != -1:
			item = self.nodes[idx]
			print_index(0, idx, 16, size=item.size)
			print_line(0, 16)
			idx = self.next(idx)
		print_index(0, -1, 16, size=-1)
		print_line(0, 16)

	def get_item(self, idx):
		return self.nodes[idx]

	def reallocate(self, idx, size):
		while self.next(idx) != -1 and size > 0:
			size = size - self.max_block_size
			idx = self.next(idx)

		cur_item = self.get_item(idx)
		if size <= self.max_block_size:
			cur_item.set_size(size)
		else:
			cur_item.set_size(self.max_block_size)
		size = size - self.max_block_size
		prev_idx = idx

		while size > 0:
			item = self.allocate()
			self.link(prev_idx, item.current)
			if size < self.max_block_size:
				item.set_size(size)
			else:
				item.set_size(self.max_block_size)
			size -= self.max_block_size
			prev_idx = item.current

	def release(self, idx):
		if idx is None or idx == -1:
			return
		self.release(self.next(idx))
		self.nodes[idx].current = -1
		self.nodes[idx].next = -1


class Block(object):
	"""
	the disk storage block
	the base class of group block and empty block
	"""
	__metaclass__ = abc.ABCMeta

	def __init__(self, idx):
		self._index = idx

	@property
	def index(self):
		"""
		get the block index
		"""
		return self._index

	@index.setter
	def index(self, value):
		self._index = value

	@abc.abstractmethod
	def display(self, deep):
		raise NotImplementedError("No Need Implemented")


class GroupBlock(Block):
	"""
	the group leader block
	the first item is the block size, the second item is a index to GroupBlock
	the rest item is index to EmptyBlock
	"""
	def __init__(self, idx, block_size):
		super(GroupBlock, self).__init__(idx)
		self._size = block_size
		self.items = []

	def __getitem__(self, key):
		"""
		get specific block
		"""
		if key >= self.size:
			raise NotImplementedError("Not Implemented Yet")
		return self.items[key]

	def __setitem__(self, key, value):
		if key >= self.size:
			raise NotImplementedError("Not Implemented Yet")
		self.items[key] = value

	def add_block(self, block):
		self._size += 1
		self.items.append(block)

	def remove_block(self):
		self._size -= 1
		self.items.pop()

	@property
	def size(self):
		return self._size

	@property
	def blocks(self):
		return self.items

	def display(self, deep):
		print_index(deep, self.index, 16, char='~')
		print_line(deep, 16)
		print_line(deep + 1, 16)
		print_index(deep + 1, self.index, 16, char='~')
		print_line(deep + 1, 16)
		print_index(deep + 1, self.size, 16)
		print_line(deep + 1, 16)
		for block in self.items:
			block.display(deep + 1)


class EmptyBlock(Block):
	"""docstring for EmptyBlock"""
	def __init__(self, idx):
		super(EmptyBlock, self).__init__(idx)

	def display(self, deep):
		print_index(deep, self.index, 16)
		print_line(deep, 16)
		

class BlockManager(object):
	"""
	manage the block allocate and recycle
	"""
	def __init__(self, max_block_size=50):
		self.super_block = GroupBlock(0, 0)
		self.max_block_size = max_block_size

	def allocate(self):
		"""
		allocate a empty block to file
		"""
		if self.super_block.size == 1:
			block = self.super_block[0]
			block.index = 0
			self.super_block = block
		else:
			self.super_block.remove_block()
		

	def recycle(self, block_no):
		"""
		recycle an real block to empty block
		`block_no` :> block number
		"""
		if self.super_block.size == self.max_block_size:
			block = GroupBlock(0, 0)
			self.super_block.index = block_no
			block.add_block(self.super_block)
			self.super_block = block
		else:
			self.super_block.add_block(EmptyBlock(block_no))

	def display(self):
		"""
		display the block in the console
		"""
		if self.super_block.size < 1:
			return

		print_line(0, 16)
		print_index(0, self.super_block.size, 16)
		print_line(0, 16)
		for block in self.super_block.items:
			block.display(0)


if __name__ == "__main__":

	fat = FAT(1024)
	item = fat.allocate()
	fat.reallocate(item.current, 4096)

	fat.release(item.current)

	new_item = fat.allocate()
	fat.reallocate(new_item.current, 812)

	fat.display(item.current)

	fat.display(new_item.current)

	fat.reallocate(item.current, 9028)
	fat.display(item.current)