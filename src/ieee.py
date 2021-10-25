# # # n = 5
# # # available = [(1, 5), (1, 5), (1, 5), (1, 5), (1, 5)]
# # #
# # #
# # #
# # # class Max_Chunks_To_Make_Sorted:
# # #     def init(self,s):
# # #         res = []
# # #         total = n
# # #         self.back_traking(s,[],res)
# # #         return self.check(res)
# # #
# # #
# # #
# # #
# # #
# # #     def back_traking(self,s,path,res):
# # #         if not s:
# # #             res.append(path)
# # #             return
# # #         for i in range(1,len():
# # #                 self.back_traking(s[i:],path+[s[:i]],res)
# # #
# # #
# # # def doctor(n, available):
# # #     min = 1
# # #     max = n
# # #     appointment = []
# # #     # [0 for _ in range(n)]
# # #     for i in range(n):
# # #         for i in range(min,)
# # #
# # #
# # #
# # #         av = available[i]
# # #          av[0] in range(min, max + 1) and av[0] not in appointment:
# # #             appointment.append(av[0] )
# # #             continue
# # #         if av[1] in range(min, max + 1) and av[1] not in appointment:
# # #             appointment.append(av[1] )
# # #
# # #     print(appointment)
# # #     if len(appointment) < n:
# # #         return -1
# # #
# # #     return appointment
# # #
# # #
# # # print(doctor(n, available))
# #
# # n = 3
# # x = [[1],[2],[3],[4]]
# # n = [(0,3),(1,5)]
# # def doctor(x,n):
# #     for l,i in x:
# #         for j in range():
# #             if j not in i:
# #                 x[l] = x[l].append(j)
# #
# #      for i in x:
# #          if len(i) == n:
# #              print(i)
# #     return "impossible"
# #
# #
# #
#


#
#
# def doctor_appointments(n,available):
#
#     for i in range(1,n+1):
#
#
#
#
# def doctor_appointments(n, available,start,stop):
#
#     a = [[1],[2],[3]]
#     for i in range(1,n):
#         for j in range(start,stop+1):
#             a = [[j]+[a]if j not in a for i in a]

#     available = sorted(available, key=lambda x: x[-1])
#     min = 1
#     max = n
#     appointment = []
#
#     for i in range(n):
#         av = available[i]
#         if av[0] in range(min, max + 1) and av[0] not in appointment:
#             appointment.append(i + 1)
#             continue
#         if av[1] in range(min, max + 1) and av[1] not in appointment:
#             appointment.append(i + 1)
#
#     if len(appointment) < n:
#         return 'impossible'
#
#     return ' '.join([str(i) for i in appointment])
#
#
# cases = int(input())
#
# for case in range(cases):
#     n = int(input())
#     available = []
#
#     for _ in range(n):
#         available.append(tuple(map(int, input().split(' '))))
#
#     # print(n, available)
#     print(doctor_appointments(n, available))
#
# #
# #
# #
# #
#
#
#
#
#
#             # # class Max_Chunks_To_Make_Sorted:
#             # #     def init(self,s):
#             # #         res = []
#             # #         total = n
#             # #         self.back_traking(s,[],res)
#             # #         return self.check(res)
#             # #
#             # #
#             # #
#             # #
#             # #
#             # #     def back_traking(self,s,path,res):
#             # #         if not s:
#             # #             res.append(path)
#             # #             return
#             # #         for i in range(1,len():
#             # #                 self.back_traking(s[i:],path+[s[:i]],res)
