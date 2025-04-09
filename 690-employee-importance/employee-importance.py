"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(Employee)
        for emp in employees:
            graph[emp.id] = emp
        def dfs(employee):
            total_import = 0
            for subid in employee.subordinates:
                total_import += dfs(graph[subid])
            return total_import + employee.importance
        for emplo in employees:
            if emplo.id == id:
                return dfs(emplo)