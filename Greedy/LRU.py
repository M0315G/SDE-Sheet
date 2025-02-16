# Question:
# In operating systems that use paging for memory management, page replacement algorithm is needed to decide which page needs to be
# replaced when the new page comes in. Whenever a new page is referred and is not present in memory, the page fault occurs and
# Operating System replaces one of the existing pages with a newly needed page.
# Given a sequence of pages in an array pages[] of length N and memory capacity C, find the number of page faults using
# Least Recently Used (LRU) Algorithm. 

# Logic:
# simple list based implementation of the LRU algorithm.

class Solution:
    def pageFaults(self, N, C, pages):
        faults = 0
        p = []
        for page in pages:
            # print(f"For page: {page}")
            if page in p:
                # print("Found")
                p.remove(page)
                p.append(page)
            else:
                # print("Not douns")
                if len(p) == C:
                    p.pop(0)
                p.append(page)
                faults += 1
            # print(p)
        return faults