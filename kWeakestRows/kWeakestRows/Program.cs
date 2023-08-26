using System;

namespace KWeaskestRows
{
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
    internal class Program
    {
        static void Main()
        {
            //int[][] matrix = new int[4][];
            //matrix[0] = new int[3] { 1, 1, 1 };
            //matrix[1] = new int[3] { 1, 1, 1 };
            //matrix[2] = new int[3] { 1, 1, 0 };
            //matrix[3] = new int[3] { 1, 0, 0 };

            //int[][] matrix = new int[4][];
            //matrix[0] = new int[3] { 0, 0, 0 };
            //matrix[1] = new int[3] { 0, 0, 0 };
            //matrix[2] = new int[3] { 0, 0, 0 };
            //matrix[3] = new int[3] { 0, 0, 0 };

            int[][] matrix = new int[4][];
            matrix[0] = new int[3] { 1, 1, 1 };
            matrix[1] = new int[3] { 1, 1, 1 };
            matrix[2] = new int[3] { 1, 1, 1 };
            matrix[3] = new int[3] { 1, 1, 1 };


            foreach (var entry in Solution.KWeakestRows(matrix, 1))
            {
                Console.Write(entry + ", ");
            }
            
            Console.ReadLine();
        }
    }
}


