class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.result = []
        for l in vec2d:
            self.result += l

    def next(self):
        """
        :rtype: int
        """
        return self.result.pop(0)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.result) >0
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())


# follow up (Java)
# public class Vector2D implements Iterator<Integer> {
#     private Iterator<List<Integer>> i;
#     private Iterator<Integer> j;

#     public Vector2D(List<List<Integer>> vec2d) {
#         i = vec2d.iterator();
#     }

#     @Override
#     public Integer next() {
#         hasNext();
#         return j.next();
#     }

#     @Override
#     public boolean hasNext() {
#         while((j == null || !j.hasNext()) && i.hasNext()){
#             j = i.next().iterator();
#         }
#         return j != null && j.hasNext() ;
#     }
# }

/**
 * Your Vector2D object will be instantiated and called as such:
 * Vector2D i = new Vector2D(vec2d);
 * while (i.hasNext()) v[f()] = i.next();
 */