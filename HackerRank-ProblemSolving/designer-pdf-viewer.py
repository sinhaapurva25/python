def designerPdfViewer(h, word):
    # Write your code here
    return max([h[ord(i)-ord('a')] for i in word])*len(word)
designerPdfViewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7],'zaba')