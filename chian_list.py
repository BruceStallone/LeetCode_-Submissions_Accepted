class Node:
	"""基本描述
	链表，是由一系列节点组成的元素集合。
	每个节点包含2部分：1.数据域。2.指向下一个节点的指针next
	通过节点之间的相互连接，最终串联成一个链表
	节点P插入方法：
	p.next = cur_node.next
	cur_node.next = p
	节点p的删除方法：
	p = cur_node.next
	cur_node .next = cur_node.next.next (= p.next)
	del p
	"""
	def __init__(self, item):
		"""
		单链表
		"""
		self.item = item
		self.next = None # 默认属性，指向下一个节点的指针

def creat_linklist_head(li):
	"""
	创建链表,头插法
	"""
	head = Node(li[0])
	for element in li[1:]:
		node = Node(element)
		# 头插法，原来的头部变成第二个节点，新的变成头部
		node.next = head
		head = node
	return head

def creat_linklist_tail(li):
	"""
	创建链表，尾插法
	"""
	head = Node(li[0])
	tail = head
	for element in li[1:]:
		# 头插法，原来的尾部变成第倒数二个节点，新的变成尾部
		tail.next = node
		tail = node
	return head


class BidNode:
	"""基本描述
	双向链表
	每个节点包含3部分：
	1.数据域。
	2.指向下一个节点的指针next。
	3.指向前一个节点的指针
	节点P插入方法：
	p.next = cur_node.next
	cur_node.next.prior = p
	p.prior = cur_node
	cur_node.next = p
	节点p的删除方法：
	p = cur_node.next
	cur_node.next = cur_node.next.next(= p.next)
	p.next.prior = cur_node
	del p
	"""
	def __init__(self, item):
		"""
		单链表
		"""
		self.item = item
		self.next = None # 默认属性，指向下一个节点的指针
		self.prior = None # 默认属性 指向上一个节点的指针