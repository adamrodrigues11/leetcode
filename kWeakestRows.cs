public class Solution
{
    public static int[] KWeakestRows(int[][] mat, int k)
    {
        HashSet<int> rowIndices = new HashSet<int>();
        for (int i = 0; i < mat.Length; i++)
        {
            rowIndices.Add(i);
        }

        int[] weakestRows = new int[k];
        int resultIndex = 0;
        for (int j = 0; j < mat[0].Length; j++)
        {
            foreach (int i in rowIndices)
            {
                if (mat[i][j] == 0)
                {
                    weakestRows[resultIndex] = i;
                    resultIndex++;
                    rowIndices.Remove(i);
                    if (resultIndex == k) break;
                }
            }
            if ( resultIndex == k ) break;
        }
        // If we get through the loop with an incomplete result array due to rows of all 1s, execute the following
        if ( resultIndex < k )
        {
            foreach ( int i in rowIndices )
            {
                weakestRows[resultIndex] = i;
                resultIndex++;
                if ( resultIndex == k ) break;
            }
        }
        return weakestRows;
    }
}

// this works but needs some serious optimization
// actually, I may have just been lucky as the hashset is not guaranteed to be ordered - better to use an array or list
// I tried to get fancy by not checking rows that had already been checked and not checking columns that had already been checked but it got way too confusing and lots of cases to consider

// better solutions would include summing each row (and stopping when you get to a 0) and then sorting the rows by their sums, taking the index of the first k rows


// using priority queue (from leetcode)
// PriorityQueue does not guarantee FIFO order for elements with the same priority ... hence the addition of row / rows to the strength
// it also dequeues from lowest to highest priority
public class Solution {
    public int[] KWeakestRows(int[][] mat, int k) {
        PriorityQueue<int, double> rankings = new PriorityQueue<int, double>();
        int[] weakest = new int[k];
        int rows = mat.Length;

        for(int row = 0; row < rows; row++) {
            int strength = mat[row].Sum();
            rankings.Enqueue(row, strength + ((double)row / rows));
        }

        for (int check = 0; check < k; check++) {
            weakest[check] = rankings.Dequeue();
        }

        return (weakest);
    }
}

// using Linq methods from Enumerable since Array class implements IEnumerable (from leetcode)
// this is wicked fast and very readable
public class Solution {
    public int[] KWeakestRows(int[][] mat, int k) {
        return mat
                .Select((row, i) => new { score = row.Sum(), index = i })
                .OrderBy(r => r.score)
                .Select(r => r.index)
                .Take(k)
                .ToArray();
    }
}

