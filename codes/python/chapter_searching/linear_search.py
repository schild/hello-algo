"""
File: linear_search.py
Created Time: 2022-11-26
Author: timi (xisunyy@163.com)
"""

import sys, os.path as osp

sys.path.append(osp.dirname(osp.dirname(osp.abspath(__file__))))
from modules import *


def linear_search_array(nums: list[int], target: int) -> int:
    """线性查找（数组）"""
    return next((i for i in range(len(nums)) if nums[i] == target), -1)


def linear_search_linkedlist(head: ListNode, target: int) -> ListNode | None:
    """线性查找（链表）"""
    # 遍历链表
    while head:
        if head.val == target:  # 找到目标节点，返回之
            return head
        head = head.next
    return None  # 未找到目标节点，返回 None


"""Driver Code"""
if __name__ == "__main__":
    target = 3

    # 在数组中执行线性查找
    nums = [1, 5, 3, 2, 4, 7, 5, 9, 10, 8]
    index: int = linear_search_array(nums, target)
    print("目标元素 3 的索引 =", index)

    # 在链表中执行线性查找
    head: ListNode = list_to_linked_list(nums)
    node: ListNode | None = linear_search_linkedlist(head, target)
    print("目标节点值 3 的对应节点对象为", node)
