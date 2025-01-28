# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()  # Geçici bir dummy oluşturur
        current = dummy  # Mevcut düğümümüz dummy ile başlıyor

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next  # Mevcut düğümü güncelle

        # Eğer list1 veya list2 kaldıysa, doğrudan ekle
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next  # Dummy'nin başını değil, sonraki elemanı döndür
