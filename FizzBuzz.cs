public class Solution {
    public IList<string> FizzBuzz(int n) {
        var output = new List<string>();
        for ( int k = 1; k <= n; k++ ) {
            string elem = "";
            if ( k % 3 == 0 ) {
                elem += "Fizz";
            }
            if ( k % 5 == 0 ) {
                elem += "Buzz";
            }
            if ( elem.Length == 0 ) {
                elem += k.ToString();
            }
            output.Add(elem);
        }
        return output;
    }
}

public class Solution {
    public IList<string> FizzBuzz(int n) {
        var output = new List<string>();
        for ( int k = 1; k <= n; k++ ) {
            if ( k % 3 != 0 && k % 5 != 0 ) {
                output.Add(k.ToString());
                continue;
            }
            string elem = "";
            if ( k % 3 == 0 ) {
                elem += "Fizz";
            }
            if ( k % 5 == 0 ) {
                elem += "Buzz";
            }
            output.Add(elem);
        }
        return output;
    }
}


// gets much better performance than the above two solutions
// probably because using fixed length array instead of list
public class Solution {
    public IList<string> FizzBuzz(int n) {
        var output = new string[n];
        for ( int k = 1; k <= n; k++ ) {
            if ( k % 3 != 0 && k % 5 != 0 ) {
                output[k - 1] = (k.ToString());
                continue;
            }
            string elem = "";
            if ( k % 3 == 0 ) {
                elem += "Fizz";
            }
            if ( k % 5 == 0 ) {
                elem += "Buzz";
            }
            output[k - 1] = elem;
        }
        return output;
    }
}

